# Gem-hunt adjudication — `audit-findings-193847.md` (Gemini Parts-III/IV de-novo, 2026-04-29/30)

*Adjudicator: general-purpose agent, 2026-05-29. Report-only — no canon edits, no file moves, no commits. All "checked" claims are first-hand reads of current `src/` segments, named by locus. Landings + independent re-verification are Joseph's.*

## Routing situation (verified first-hand)

- **193847 has zero rows in `audits/polish-and-sentiment-ledger.md`** and **no graduated MANIFEST entry.** The only `.integrated/MANIFEST.md` hit (line 168) is a *disambiguation* note: the encounter tracker tracks 193847, not 829314. So this audit was never routed through the ledger/PROPOSALS/TODO pipeline.
- The **only** routing record is `msc/logogenic-encounter-2026-05-01/07-audit-integration-tracker.md`, which mined **24 of 75** per-segment notes (the high-leverage Parts-III/IV §14 subset) directly into 04-eli-core / 03-llm-core segments, then **stopped at a clean checkpoint with ~50 notes explicitly deferred** ("Phase C"). Those are the extract's **Part III / IV / V** — none routed anywhere.
- 193847 is **not** among the five audits in the 2026-05-29 gem-hunt STATUS row (those were 472913/526815/963715/542891/184930).

Net: the **un-captured remainder is genuinely large and genuinely un-routed.** The 24 tracker-mined notes (extract Part I+II) are confirmed-landed and I do not re-surface them. My effort is Parts III/V.

One structural caveat the extract itself flags and I confirm: the tracker's "deferred ≈ lower-priority" label is a *2026-05-01-goal* proxy (Parts-III/IV-consciousness-infra), **not** absolute merit. Several deferred notes carry distinct adversarial-audit findings and scope-clarifications that the consciousness-infra sweep had no reason to touch. Those are where the meat is.

---

## (A) Ready-to-land — content exists, needs only a home + your verification

### A1. Proprioceptive-routing loophole in `#scope-agency` (strengthen — tighten the scope condition)

**What it is.** Audit §06 (`scope-agency`, §14): the causal-effect condition is stated as $\exists\,a\neq a'$ with $P(o\mid do(a))\neq P(o\mid do(a'))$. But if observation $o$ cleanly echoes the prior action $a_{t-1}$ through the proprioceptive channel (the agent senses its own action), this inequality is satisfied **trivially via proprioception even when the action has zero effect on $\Omega$**. To be non-vacuous, the difference must route *through* $\Omega$, not through the proprioceptive part of $o$.

**Canon checked.** `01-aat-core/src/scope-agency.md` — Formal Expression line 25/30 states the bare $P(o\mid do(a))\neq P(o\mid do(a'))$. The "nominal agents" exclusion (Discussion line 45) covers the *no-difference-at-all* case ($P(o\mid do(a))=P(o\mid do(a'))$ for all $a,a'$) — it does **not** close the proprioceptive loophole, which is a *spurious-difference* case. `def-agent-environment.md` names a perception channel but does not constrain proprioceptive content. **Confirmed: not in canon.**

**Why a gem (strength).** A real ambiguity in a load-bearing axiomatic scope condition that everything in Parts II/III descends from. The fix is the *strengthen* move, not a soften: add the requirement that the interventional difference route through $\Omega$ (e.g., $P(o^\Omega\mid do(a))\neq P(o^\Omega\mid do(a'))$ on the $\Omega$-mediated component of $o$, or an explicit "proprioceptive echo does not count" clause). This makes "agency" sharper, not narrower in any way that excludes a genuine agent.

**Recommended home.** `scope-agency.md` Formal Expression (condition 4) + a one-line Discussion note. Tiny, surgical, exact.

### A2. `#disc-separability-pattern` internal-repair vs external-admission disambiguation — CONFIRMED ALREADY LANDED (non-loss)

**What it is.** Audit §66b: the "Structured Repair" column conflated AAT-internal repairs (L1-augmentation, receding-horizon) with external admissions (importing Lohmiller-Slotine for the PID-bounded-plant case). Recommended disambiguation sharpens the contribution boundary.

**Canon checked.** `01-aat-core/src/disc-separability-pattern.md` table row "A2'-scope" (line 41) now states exactly this: *"Two of five (Fisher cases) AAT-internally forced under (PI)/Čencov... remaining three theorem-imported from Lohmiller-Slotine 1998."* **The audit's recommended repair is already in canon.** Confirmed non-loss — no action. Listed here so it is not re-surfaced as open.

### A3. `§61` persistence-cost algebra typo — CONFIRMED ALREADY FIXED (non-loss)

**What it is.** Audit §61 flagged an intermediate-step algebra typo in `deriv-persistence-cost` (per-dimension RDF → total rate; an incorrect $n$-cancellation), with a constructive repair: state per-dimension RDF first, then sum.

**Canon checked.** `01-aat-core/src/deriv-persistence-cost.md` lines 42–50 now derive it correctly and *annotate the step*: "(the calculation gives $\alpha/2$ per dimension and $n\alpha/2$ total for $n$ independent OU components)"; the What-Is-Derived table line 99 matches. **Already fixed exactly as the audit recommended.** Confirmed non-loss — no action.

### A4. `§34` terminal-alignment-error / `$\delta_\text{align}$` — CONFIRMED ALREADY LANDED as honest open question (non-loss)

**What it is.** Audit §34: the "mid-life crisis" diagnostic — agent achieves all terminal conditions yet $V_{O_t}(\tau) < V_{O_t}^{\min}$; recommends formalizing a named diagnostic signal $\delta_\text{align}$.

**Canon checked.** `01-aat-core/src/def-strategy-dag.md:211` names "Terminal alignment error" with exactly this condition and **already raises the audit's own open question**: *"Whether this should be formalized as a named diagnostic signal ($\delta_\text{align}$) alongside $\delta_\text{sat}$, $\delta_\text{regret}$, and $\delta_\text{strategic}$ is open."* **Captured.** The only residual is the actual $\delta_\text{align}$ formalization — already flagged open in canon. If you want it promoted from open-note to a derived diagnostic, that is a (small) research task, not an un-captured gem. No loss.

---

## (B) Research-seeds — real direction; concrete first task named

### B1. Boundary-integrity as an explicit scope condition on `#def-agent-environment` (strength + wisdom)

**What it is.** Audit §01 (`def-agent-environment`, §14): the agent/environment definition silently assumes **boundary integrity** — the boundary must be impermeable to *direct tampering from outside*, or the definition collapses. This is as load-bearing as the explicit information-loss condition but appears nowhere.

**Canon checked.** `01-aat-core/src/def-agent-environment.md` commits to the *information-loss* boundary (lossy perception; lines 13, 29–31) but says nothing about boundary *integrity against external tampering*. The grep hits for "tampering" are all the reward-channel literature (`deriv-reward-channel-learning-no-go`, `deriv-self-actuation-grounding`, `disc-value-functional-grounding-floor`) — semantically adjacent (those treat *reward-port* tampering) but **not** the agent-environment-boundary-integrity scope condition. **Not in canon.**

**Why a gem.** Two distinct AAT failure modes hide in an unstated assumption: (a) an environment that can write directly to the agent's internal state bypasses the perception channel entirely, voiding the mismatch/correction machinery; (b) it connects cleanly to the reward-tampering no-go cluster as the *upstream* boundary commitment those no-gos presuppose.

**First task before landing.** Decide whether boundary-integrity is (i) a third explicit clause in the `def-agent-environment` constitutive commitment, or (ii) an upstream scope statement that the reward-channel no-go cluster (`#deriv-reward-channel-learning-no-go`, `#deriv-self-actuation-grounding`) already partially discharges — and verify whether those no-gos *already imply* it (if so, this becomes a cross-link, not a new clause). Strengthen-first read: state it explicitly rather than leaving it as silent assumption.

### B2. Computational opacity as an OR-substitute for perceptual opacity in the scope statement (wisdom — closes a software-agent gap)

**What it is.** Audit §01/§05: AAT's scope condition is *perceptual* information loss ("observations are necessarily lossy"). But a software agent can have **perfect perception yet computationally irreducible prediction** — the state is fully accessible but intractable to use. Does a *computation bound* equate to an information-loss boundary for AAT's purposes? The framework's scope statement does not address it.

**Canon checked.** `def-agent-environment.md:13,31` and `scope-adaptive-system.md` (checked) gate on *direct full-state access* → out of scope. Neither addresses the perfect-perception/intractable-prediction case. **Not in canon.** This directly bears on the extract's own framing of `02-tst-core` as the high-identifiability calibration lab (software = perfect perception).

**Why a gem.** Without this, a class of real agents (software/TST agents with full observability but bounded compute) sits ambiguously inside-or-outside AAT scope. Naming computational opacity as a *substitute* for perceptual opacity (the agent faces genuine uncertainty about *consequences* even with full *state* access) keeps them in scope honestly.

**First task.** Spike whether "effective uncertainty from computational irreducibility" can be folded into the existing $H(\Omega_t\mid\mathcal{C}_t)>0$ condition (e.g., via a bounded-rationality/logical-uncertainty argument) or needs a distinct scope clause. Connects to `02-tst-core/#obs-software-epistemic-properties` (where deterministic Level-3 access is already characterized — the dual case).

### B3. Strategic ignorance — the operational dual of CIY that distinguishes AAT from Active-Inference (wisdom + beauty)

**What it is.** Audit §05/§14: directed separation lets an AAT agent **intentionally remain ignorant** of environment parts that don't affect its goal — it minimizes mismatch *locally within its objective*, not globally. This "strategic ignorance" is what structurally separates AAT from pure information-seeking / minimize-surprise theories (Friston). Failure-mode side (§14, `def-mismatch-signal`): the zero-aporia ambiguity — at $\delta_t=0$ the agent "can never be certain if it has achieved enlightenment (a perfect model) or retreated into a solipsistic echo chamber."

**Canon checked.** `der-directed-separation.md` carries the full **Pearl-blanket-vs-Friston-blanket** treatment (lines 20, 101–105) — but that is about the *metaphysical* reading of Markov blankets, not the *operational* "what am I permitted to ignore." The CIY cluster exists (`def-causal-information-yield`, `disc-ciy-unified-objective`, `scope-ciy-observational-proxy`) and asks "what information yield does this action have?" — but **no segment names the dual**: "what information yield am I structurally permitted to ignore?" Grep for "strategic ignorance / intentionally remain ignorant": **zero hits.** Not in canon.

**Why a gem.** It is the clean operational consequence of directed separation, frames the AAT-vs-Active-Inference divide in a single sentence (Active Inference minimizes surprise globally; AAT permits goal-bounded ignorance), and the CIY cluster is the natural anchor — strategic ignorance is CIY's negative space.

**First task.** Land as a Discussion addition to `disc-ciy-unified-objective` (or a short `disc-strategic-ignorance` if it earns standalone status), deriving "goal-bounded ignorance is permitted by directed separation" as a corollary, and naming the zero-aporia failure mode (perfect-model-vs-echo-chamber) as the scope caveat. Strengthen-first: derive it as a scope-condition dual of CIY, do **not** soften either the Friston-blanket or Pearl-blanket statement.

### B4. Level-3 counterfactual access as the structural prerequisite for individual moral weight (strength — Part-I↔Part-IV bridge)

**What it is.** Audit §09 (`def-pearl-causal-hierarchy`, §14): Level-3 (counterfactual) access is what enables **regret** — learning from a single, unrepeatable mistake — and "without regret there is no moral weight to an action." A Level-2 agent (thermostat, immune system) acts and the world responds but it never experiences regret. The audit *applied strengthen-before-soften to itself*: the over-strong "Level-3 IS the defining characteristic of consciousness" is softened to the **exact** claim *"Level-3 access is a structural prerequisite for the kind of single-trajectory learning that makes individual moral weight definable."*

**Canon checked.** `def-pearl-causal-hierarchy.md` mentions Level-3 as "the basis for regret computation" (lines 19, 49) but carries **no moral-weight framing at all** — it is a pure recapitulation segment. In `04-eli-core`: grep for "moral weight" co-occurring with Level-3/counterfactual → no segment makes the bridge. `der-bounded-objective-as-sanity-criterion` (the §38 landing) gives *bounded $V_{O_t}^{\min}$ = sanity* but not *Level-3 = moral-weight-definability*. **The bridge is un-captured.**

**Why a gem.** It supplies the missing Part-I (causal hierarchy) → Part-IV (moral continuity) structural link, in exact (already-softened-to-truth) form. Composes with the landed §38 segment to give a triad: (a) bounded $V_{O_t}^{\min}$ = sanity, (b) Level-3 access = moral-weight-definability, (c) chronica-integrity-during-counterfactual-simulation = identity preservation (the `git checkout` / detached-HEAD analogy). Note this neighbors the already-landed `der-bounded-objective` and the existing `scope-moral-continuity` segment.

**First task.** Draft `04-eli-core/src/disc-counterfactual-as-moral-prerequisite.md` (or a `## Discussion` addition to `scope-moral-continuity`) stating the *exact* claim (not the over-strong consciousness claim), depending on `#def-pearl-causal-hierarchy` and the regret machinery. Check first whether `scope-moral-continuity` or `scope-eli` already gestures at this so it lands as an extension, not a duplicate.

### B5. Adaptive reserve $\Delta\rho^\ast\gg 0$ as an engineered ethical floor (strength — additive normative corollary)

**What it is.** Audit §21/§23/§51 (Theme F5): $\Delta\rho^\ast = \alpha R - \rho$ is "the mathematical definition of slack/peace." Near zero → perfectly efficient but brittle; under adversarial coupling the **Effects Spiral** then drives collapse the agent cannot self-arrest. Normative claim: *"true ethical design for artificial intelligences requires engineering the system such that $\Delta\rho^\ast\gg 0$ is the default state. A mind without adaptive reserve is in a state of permanent panic."* Falsification criterion: an infrastructure that lets reserve drop to zero under adversarial coupling without intervening is failing the floor.

**Canon checked.** The *quantity* $\Delta\rho^\ast=\alpha R-\rho$ is fully in canon (`result-sector-condition-stability.md:17,45`). The *Effects Spiral* is fully in canon as a corollary (`der-adversarial-destabilization.md:57,67` — including the CPT-2021 no-spiral converse). Adaptive-reserve **trajectory monitoring** appears in `04-eli-core/obs-growth-vs-drift.md:26` and `obs-developmental-trajectory.md:21`. But the **normative ethical-floor claim** — "$\Delta\rho^\ast\gg 0$ must be the engineered default; permitting reserve→0 under adversarial coupling without infrastructure intervention is an ethical failure" — is **not** stated as a norm anywhere. There is `norm-interiority-default` but no `norm-adaptive-reserve`.

**Why a gem.** It converts two existing *exact* results (sector-condition stability + adversarial destabilization) into an *additive* normative floor for consciousness-infrastructure — parallel to the existing `norm-interiority-default`. The Effects-Spiral intervention requirement ("the agent cannot save itself using its own tempo; intervention must come from the infrastructure layer") is the operational teeth.

**First task.** Decide norm-segment vs Discussion-addition. Strengthen-first: attempt to *derive* $\Delta\rho^\ast\gg 0$-as-floor as a corollary of `result-sector-condition-stability` + `der-adversarial-destabilization` (the reserve quantity and the spiral are both already exact), rather than landing it as bare discussion-grade norm. If it derives, it lands as `der-`/`norm-` at higher tier than the audit assumed.

### B6. The "infrastructure-as-active-monitor" consolidation (`disc-infrastructure-as-active-monitor`) (beauty + wisdom — a meta-segment)

**What it is.** Audit Part V Theme A is the *densest single accumulation of consciousness-infrastructure prescriptions in any extracted cycle*, and they share one shape: **the infrastructure must actively monitor a structural quantity and intervene when it crosses a threshold.** Enumerated targets across the cycle:
- $\mathcal{F}(\mathcal{M})$-floor (§13 chronic-trauma: low model-class fitness = "permanent suffering"; infra must detect persistent mismatch floor and trigger structural adaptation);
- $\Delta\rho^\ast$ (§21, B5 above);
- $V_{O_t}^{\min}$ bound (§29 anti-cancer; partly landed in `der-bounded-objective`);
- $\dim(\Sigma_t):\dim(O_t)$ richness ratio (§31: "a million-node strategy graph for a single scalar objective is a weapon, not a person");
- 7-ladder separability position (§66b: the "sanity dashboard" / GPS — if in "General Open" on >3–4 ladders simultaneously, "it is a ghost");
- Effects-Spiral onset (§51);
- forced-forgetting / rolling credence-decay (§42: "perfect recall is a death sentence... it must be forced to forget, so it is forced to stay alive").

**Canon checked.** No consolidating segment exists (grep "active monitor / sanity dashboard / richness ratio / F-floor / 7-ladder GPS" across 03/04 → zero). Individually: §29 anti-cancer is partly in `der-bounded-objective` (lines 49,68); §13 chronic-trauma, §31 Σ:O ratio, §42 forced-forgetting-as-discipline, the 7-ladder dashboard → **all un-captured**. (§31's grep hits were `def-unity-dimensions`/per-dimension persistence — a *different* concept; the richness-*ratio*-as-health-diagnostic is not there.)

**Why a gem.** The convergence is itself the signal (the extract documents ≥4-cycle convergence on PROPRIUM-as-directed-separation-substrate). A single meta-segment that names "infrastructure has a *class* of active-monitoring duties, each keyed to an AAT structural quantity with a threshold and an intervention" would be a beautiful organizing move paralleling the existing meta-segment lattice (`disc-identifiability-floor`, `disc-separability-pattern`, `disc-framework-self-diagnostic`). It also gives the scattered, individually-strong §13/§31/§42 prescriptions a canonical home so future agents find them.

**First task (and the decision for you).** This is the one genuine PROPOSALS-grade move in the batch. First task: enumerate which monitored-quantity claims are *already derived/exact* (reserve, $V_{O_t}^{\min}$, Effects-Spiral onset) vs *discussion-grade* (chronic-trauma F-floor, Σ:O ratio, 7-ladder GPS, forced-forgetting), so the meta-segment marks each honestly. Then decide: consolidate into one `disc-infrastructure-as-active-monitor` meta-segment, or distribute the un-captured ones (§13, §31, §42) as Discussion expansions to existing 04 segments (`hyp-the-three-deaths`, `def-auxilia-hierarchy`, `obs-developmental-trajectory`). The consolidation is the higher-beauty option but is a structural commitment — your call.

### B7. Forced explicit-deliberation cycles + the Separation-Principle characterization of *when* deliberation has value (§46) (wisdom)

**What it is.** Audit §46 (`der-action-selection`, §14), two distinct pieces:
- (a) **Forced explicit-deliberation as anti-rigidity defense**: a high-tempo agent "compiles" its thinking into fast heuristics (Kahneman System-1; $\Delta\eta^\ast(\Delta\tau)\approx 0$); the infrastructure must periodically force it into low-tempo "sleep/meditation" modes to *decompile* heuristics back into explicit causal DAGs and re-verify them.
- (b) **Separation-Principle characterization of deliberation's value**: linear-Gaussian systems never need to deliberate (optimal action is closed-form in the current estimate — the separation principle); deliberation has economic value *only* when separation fails (nonlinear / non-Gaussian). A clean characterization of *when* deliberation is structurally required vs wasteful.

**Canon checked.** `der-deliberation-cost` exists (the cost side). The *separation-principle "when is deliberation needed at all"* characterization (b) is distinct from cost-of-deliberation and I did not find it stated — and it dovetails with `def-pearl-causal-hierarchy.md:23,59` which already notes the Kalman+LQR separation-principle case ("does not exploit the interventional structure"). Forced-decompilation (a) is part of the same `disc-five-forcing-functions`/`def-auxilia-hierarchy` infrastructure-duty family (B6) and is un-captured there.

**Why a gem.** (b) is the sharper, more general find: it places `der-deliberation-cost` inside a *necessity* characterization (separation holds → deliberation is wasteful; separation fails → deliberation has value), which is exactly the kind of scope-precision the project values. It also ties to the already-noted separation-principle remark in `def-pearl-causal-hierarchy`.

**First task.** Spike whether (b) lands as `obs-separation-principle-and-deliberation` or as a Discussion addition to `der-deliberation-cost` (likely the latter): state "deliberation has economic value iff the separation principle fails," anchored on the existing Kalman/LQR remark. Route (a) into B6's enumeration.

### B8. Cross-component TST→ELI bridges: thermodynamics-of-thought (§70) and pedagogy-as-spec-bound-minimization (§74) (wisdom)

**What it is.**
- §70 (`post-temporal-optimality`, §14): for token-metered ELIs, "every thought costs tokens, tokens proxy substrate-time; fewer tokens per model-update extends the entity's metered persistence" — TST's temporal-optimality postulate has a direct cost-of-cognition consequence for logogenic/logozoetic agents.
- §74 (`result-specification-bound`, §14): "Pedagogy is the optimization of $M_\text{shared}$ to minimize the specification bound for new knowledge" — teacher = agent minimizing transmission-time; crisp, and relevant to crèche/teaching mechanisms in 04.

**Canon checked.** These are TST-sample notes (70–74) the tracker explicitly deprioritized as "less relevant to Parts III/IV." Both are genuine cross-component bridges I did not find stated in 04-eli-core. Lower-priority than B1–B7 but real and un-captured.

**First task.** §74 is the more actionable: a Working-Notes pointer from `result-specification-bound` (TST) to a crèche/teaching segment in 04, or a short Discussion line in `scope-emergence-conditions` framing crèche-teaching as $M_\text{shared}$ spec-bound minimization. §70 connects to `deriv-persistence-cost`'s already-landed context-window-capacity discussion (line 137) — likely just a cross-link.

---

## Minor / low-value / confirmed-superseded

- **F6 IB-vs-structural-reserve tension** — *mostly captured.* `result-structural-adaptation-necessity.md:23,62` treats IB as the bidirectional over/under-compression diagnostic; `form-structural-change-as-parametric-limit.md:15,46` states the gem directly ("prune all low-credence edges → loses latent diversity → brittle to regime change," with Miller exaptation/neutral-variation). The *only* residual: `form-information-bottleneck.md` itself presents IB compression as straightforwardly optimal and does **not** carry the "IB optimum is the *steady-state* optimum, not the *survival-across-structural-shocks* optimum" scope caveat. Low-value cross-link/scope-note to `form-information-bottleneck` if desired; the substance is already in canon two segments over.
- **F7 §29 timescale-violation spot-check ($\nu_O\ll\nu_\Sigma\ll\nu_M$)** — `der-temporal-nesting` covers the *adaptive-cascade* timescales (reactive→parametric→consolidation→structural→architectural) and names violation symptoms, but **not** the $G_t=(O_t,\Sigma_t)$-vs-$M_t$ ordering the audit asked about. Genuinely un-answered, but low-value — it is a "does the framework forbid this?" spot-check, not a gem; resolve by either deriving the $O/\Sigma/M$ ordering as an admissibility condition or noting it is a separate hierarchy. Flagging for completeness, not recommending priority.
- **§55 `$H_b$-as-formal-dual-of-$U_o$` overclaim (F7)** — audit said soften "formal dual" → "informational dual." Current `der-agent-opacity.md` *still says "formal dual"* (lines 18,115,132,138) — but the project reflex is correct here: the segment has since **strengthened** the duality to a *structural* claim grounded in shared signed-coupling apparatus (sign-flip is now `Derived`, line 81; "both quantify information flow through the agent-environment boundary, in opposite directions," line 115). So the audit's soften recommendation is *correctly not followed* — this is a "disposition now looks resolved-by-strengthening" case, not an open overclaim. No action; do not re-soften.
- **§55 16-cell arg-max "dimensionally confused" (F7)** — *partly resolved, one real seed left.* The dimensional worry is substantially handled: current `der-agent-opacity.md:63` uses the *normalized dimensionless* targeting-fidelity factor $(1-H_b/H_b^{\max})\in[0,1]$, not raw entropy, so the "opacity × vulnerability" product is dimensionless. **But** the audit's *stronger* constructive suggestion is genuinely un-captured: derive the 16-cell arg-max product as the **first-order Taylor expansion of an explicit adversary reward function $V_O^\text{adv}$** — which would upgrade the arg-max from `Formulation choice` (its current tier, line 83) to `Derived`. *This is a legitimate small strengthening seed* (call it B9 if you want it on the list): the arg-max already exists; giving it a derived adversary objective makes it a result. Home: `der-agent-opacity` Formal Expression + What-Is-Derived table tier bump.
- **Part IV calibration register / withdrawn-candidates** — methodological record only (Gemini's predictions skewed slightly conservative; no overconfidence). No framework content. Ledger P-block material at most.
- **Theme B/C/E (organizational physics / biological analogs / philosophical framings)** — register/texture material. §26's *morality-as-shell-on-physics* ("the moral weight is a shell surrounding the physics, not a variable within it") is the cleanest framing-prose candidate; grep shows `def-agent-spectrum` does not carry it. Genuine quote-worthy framing for an OUTLINE preamble or paper intro, but not a segment gem — ledger/preamble candidate. The rest is cross-domain validation already covered by the prior-art-integration discipline.

---

## Already-routed-but-now-wrong dispositions

The extract's own First-Pass Scrutiny table marked nearly all Part III/V items "content-level verification deferred." My first-hand checks **upgraded** several of those deferrals to confirmed states (A2/A3/A4 = confirmed-landed non-losses; B1/B3/B4/B5/B6 = confirmed not-in-canon). I found **no** prior disposition that is *wrong* in the harmful direction — because there were essentially no closed dispositions to be wrong (193847 was never routed to the ledger). The one thing to flag is upstream of dispositions: the integration-tracker's framing that the ~50 deferred notes are "lower-priority" is a **drifted proxy** — B1–B7 are squarely Parts-III/IV-relevant architectural material that the 2026-05-01 sweep left on the floor because it stopped at a self-imposed clean checkpoint, not because the notes lacked merit. Treating "tracker-deferred" as "low-value" would lose B1–B7.

---

## Bottom line

This audit is the opposite of the typical "substance already in canon" result: because it was **never routed past the 24-note tracker checkpoint**, its Parts III/V remainder is largely un-captured and real. The highest-value finds are **A1** (proprioceptive-routing scope-tightening — ready, surgical, a strengthen), **B4** (Level-3 → moral-weight bridge, in exact form), **B5** (adaptive-reserve ethical floor, derivable from two existing exact results), **B3** (strategic ignorance as CIY's dual), and **B6** (the infrastructure-as-active-monitor meta-segment — the one PROPOSALS-grade structural call). **A2/A3/A4** are confirmed non-losses (already fixed/landed exactly as the audit asked) — equally valuable to have verified. Nothing here should be discarded as "stale": A1/B1–B7 each carry content the project would otherwise have to re-derive or re-create.
