# SP-26 — "Which-parameter-responds-to-which-cause" disambiguation: corpus-wide instance sweep

**Scope:** read-only sweep of `01-aat-core/src/` (thorough), plus `02-tst-core/src/` and `03-llm-core/src/` where the pattern appears. Report + assessment only — no canon edits.

**Date:** 2026-05-29. **Method:** lexical net (`tempting | naive | conflat | mistake | double-count | category error | rather than | not X but Y | which knob`) across all three component `src/` trees, then full-segment read of every hit that survived a first-pass relevance filter, judged against the seed shape and against the three sibling/exclusion patterns named in the task.

---

## The pattern, stated precisely (so the boundary is defensible)

The seeds share a specific shape, narrower than "any definition" or "any scope condition":

> A **cause** is in play. A plausible-but-wrong modeling move would respond to that cause by turning **parameter X**. AAT shows the cause actually turns **parameter Y** (X stays put), kills the conflation in a few sentences, and the *kill* is load-bearing because X and Y route to *different repairs*.

The diagnostic that separates a true instance from an ordinary definition: **there must be a tempting wrong knob.** A definition that merely introduces a quantity is not an instance; a definition that introduces a quantity *and names the quantity it is routinely confused with, and says why turning the wrong one is the error* is an instance.

Three things are explicitly **out of scope** (siblings, not members):

- **(b) no-go-as-apparatus** — `#disc-constructive-impossibility-posture`. "Name a floor, name the unique escape, treat the no-go as load-bearing." Distinct move: it forbids an *inference*, it does not redirect a *cause* to the right *knob*.
- **(c) separability / coordinate-forcing** — `#disc-separability-pattern` (what the framework separates), `#disc-additive-coordinate-forcing` (what coordinate a uniqueness theorem forces). Distinct: forcing names what AAT *commits to*; this pattern names what a *modeller gets wrong*.
- **(a) ordinary definitions / scope conditions** — a scope condition narrows applicability; it does not necessarily kill a conflation.

A fourth boundary worth stating, surfaced by the sweep: the **inverse** move — *two distinct causes drive the same knob* (a unification, e.g. `#scope-edge-update-causal-validity`'s "observability and identifiability both freeze the edge"). That is the mirror image of this pattern, not an instance of it; noted below.

---

## Instances (graded)

### Tier 1 — clean, load-bearing, indisputably the same move as the seeds

**S1 (seed) — $\beta$-vs-$\rho$ double-counting.** `#form-information-bottleneck:15,30,32`.
- *Cause:* environmental volatility $\rho$ rises.
- *Wrong knob:* lower the IB trade-off parameter $\beta$ ("the world is volatile, so compress harder").
- *Right knob:* nothing on $\beta$ — volatility *natively* degrades $I(\mathcal{C}_t; o_{t+1:\infty})$, so the optimal $\phi^\ast$ discards stale history at constant $\beta$; $\beta$ tracks the agent's *internal* memory/compute cost. The action knob (exploration) is what responds to $\rho$.
- *Why same kind:* a real, common error ("lower $\beta$ because volatile") killed by a double-counting argument. Canonical.

**I1 — emitter-scalar vs recipient-regime.** `#der-interaction-channel-classification:23,27,159` (esp. §"Why II-a vs II-b matters").
- *Cause:* a coupling event arrives at recipient $B$ from agent $A$.
- *Wrong knob:* collapse it into one scalar disturbance increment $\gamma_A\mathcal{T}_A \to \rho_B^{\text{eff}}$ and respond uniformly with "more tempo / bandwidth."
- *Right knob:* the event lands in one of four regimes; **II-a (magnitude shock)** → more bandwidth/tempo, but **II-b (structural shock)** → a *different model class* (structural adaptation), and **more tempo does not help**; **III (ambient erosion)** → infrastructure-level filtering. "Both produce similar pain signals but admit opposite cures. Collapsing them confuses diagnosis."
- *Why same kind:* the cleanest non-seed instance. The emitter-sees-a-scalar / recipient-sees-a-regime line is exactly "the cause does not turn the knob you think." Strongest single piece of evidence that the pattern is real and recurring.

**I2 — $\kappa$ (coupling) vs $\mathcal{A}$ (ambiguity): the LLM-bias lever.** `03-llm-core/src/scope-observation-ambiguity-modulation:79,97,109`.
- *Cause:* an LLM-based (Class 3 / Coupled) agent exhibits goal-conditioned belief bias.
- *Wrong knob:* "reduce the coupling $\kappa_{\text{processing}}$." This is the natural reach (it is the coupling that causes the bias) but $\kappa\approx1$ is *architectural* — not reducible without redesigning the model.
- *Right knob:* the designer-controllable factor is observation ambiguity $\mathcal{A}(e_\tau)$ (a domain/observation-channel property): "the practical lever … is not reducing $\kappa$ … but reducing $\mathcal{A}$ (more tests, more precise metrics, more structured outputs)."
- *Why same kind:* the bias law $\propto \kappa \cdot \mathcal{A}$ separates two independent quantities and tells you which one a designer can actually turn. **Bonus:** the segment *records the conflation as a fixed bug* — "the conflation with $\mathcal{A}$ was the earlier-formulation bug Finding B identified" — so the disambiguation here is not just stylistic flourish, it is a documented correction of a real prior error. This is the pattern caught in the act. It also demonstrates the pattern is **not Part-I-local**: it lives in Part III.

### Tier 2 — genuine instances, slightly different sub-shape (two-distinct-quantities split rather than one-cause-wrong-knob)

**S3 (seed) — satisfaction-gap vs control-regret.** `#def-satisfaction-gap` / `#def-control-regret`.
- *Cause:* the goal is not being met (a positive goal-distance signal).
- *Wrong knob:* a single $\delta_{\text{objective}}$ → revise the strategy (or revise the goal) without knowing which.
- *Right knob:* the 2×2 of $\delta_{\text{sat}}$ (goal too hard) × $\delta_{\text{regret}}$ (strategy too weak) routes to *different* substates — strategy revision vs capability/objective revision. "$\delta_{\text{regret}}$ can be near zero while the agent is optimally failing." Each cell prescribes a different corrective action.
- *Why Tier 2 not Tier 1:* it splits one cause into two *orthogonal diagnostics* rather than redirecting one cause off a wrong knob — but the killed error ("a single goal-distance signal could not distinguish these") is exactly the seed's spirit.

**S2 (seed) — $\mathcal{F}$ (bias-floor) vs $S(M_t)$ (bias+estimation).** `#deriv-l1-update-bias`.
- *Cause:* edge credences under L1' correlated evidence drift / are wrong.
- *Wrong knob:* read the error as generic "bias vs variance" and treat it as estimation noise that more data fixes.
- *Right knob:* the structural bias-floor (Cramér-Rao under forgetting, `#disc-identifiability-floor` Instance 2) is *not* reducible by more data — it is a floor; the part that *is* estimation is separate. More precise than the textbook bias/variance split. Direction is preserved, *magnitude* is floored — Fisher-whitening fixes the former, not the latter.
- *Why Tier 2:* the disambiguation rides partly on an identifiability *floor* (sibling-pattern adjacency), but the live contribution — distinguishing the *kind* of error so you turn the right correction — is this pattern.

**U1 — $U_O$ (target alignment) vs $U_\Sigma$ (policy alignment) jointly control action error.** `#def-unity-dimensions:115` + `#result-unity-closure-mapping`.
- *Cause:* a composite's action error $\varepsilon_a$ is high.
- *Wrong knob:* "align the objectives" (collapse alignment to a single scalar $U_O$).
- *Right knob:* $\varepsilon_a$ tracks *both* $U_O$ (evaluation/preference agreement) *and* $U_\Sigma$ (execution-path agreement), which are physically distinct: "agents with identical objectives but different execution plans have high $U_O$, low $U_\Sigma$." You cannot fix execution-path divergence by re-aligning targets.
- *Why Tier 2:* a two-distinct-quantities split (like the seeds S2/S3) rather than a one-cause-wrong-knob. Clean and load-bearing for composite diagnosis.

**R1 — exploration: uncertainty-driven vs survival/drift-driven.** `#deriv-causal-ib-exploration:6,8`.
- *Cause:* the agent is *confident* (model uncertainty $U_M$ low) in a drifting world.
- *Wrong knob:* turn exploration *down* (the standard epistemic drive scales $\lambda_{\text{info}}\propto U_M$, so confidence says "stop exploring").
- *Right knob:* a *second*, structurally distinct drive $\lambda_{\text{surv}}\propto 1/U_M$ forces exploration precisely when confident — "confident agents are not safe agents in drifting environments." The cause (low $U_M$) turns a *different* exploration knob than the one a single-drive reading would predict.
- *Why Tier 2:* it is genuinely a which-cause-turns-which-knob recognition (two drives at opposite ends of the uncertainty axis), but it has a foot in the no-go camp (it is framed as a *structural*, not parametric, bypass of the dark-room critique). Sits at the boundary with the constructive-impossibility sibling — countable as either; counts here because the live content is "this cause drives the *other* exploration term."

### Tier 3 — partial / borderline (the move is present but entangled with a sibling pattern)

**P1 — $\kappa$-as-scalar is a category error.** `#der-directed-separation:18,99` (and CLAUDE.md §"Key Architectural Decisions" #5 names it explicitly).
- *Cause:* an architecture mixes epistemic and strategic processing.
- *Wrong knob:* treat coupling as a smooth tunable scalar $\kappa$ you dial.
- *Right knob:* a *discrete structural class* (1/2/3); $\kappa$ is only a meaningful diagnostic *within* Class 2. "This replaces an earlier $\kappa$-as-scalar framing."
- *Why Tier 3:* the move's *form* matches ("not the knob you think"), but the substance is a structural-classification commitment — closer to the framework deciding *what coordinate it uses* than to killing a modeller's cause→knob conflation. Adjacent to coordinate-forcing.

**P2 — modular-safety failure is regime change (R0→R1), not architectural-class change.** `#disc-dynamic-regime-axis:155` (+ §"Cross-axis interactions").
- *Cause:* objective divergence appears in a previously-aligned composite; modular safety guarantees fail.
- *Wrong knob:* attribute the failure to an *architectural-class change* (Class 1 → Class 2).
- *Right knob:* architectural class does **not** change under goal-blind routing; the *dynamic regime* changes (R0 contraction → R1 equilibrium). "The failure mechanism is regime change … rather than architectural-class change (which does not happen)."
- *Why Tier 3:* a clean which-knob disambiguation in its own right (two *axes*, and the cause moves you along the one you weren't watching), and it explicitly cites a "conflation diagnosis" in the spike. But it lives inside a segment whose primary job is a four-tier taxonomy; the disambiguation is a consequence the axis surfaces rather than the segment's spine. Real instance, secondary placement.

**P3 — codebase-$\rho$ vs full-$\Omega$-$\rho$.** `02-tst-core/src/obs-software-epistemic-properties:26`.
- *Cause:* you want to estimate disturbance rate $\rho$ for a software agent.
- *Wrong knob:* compute $\rho$ over the codebase only.
- *Right knob:* "Restricting $\Omega$ to source code … systematically underestimates disturbance; the theory should be applied to codebase-disturbance and non-codebase-disturbance separately."
- *Why Tier 3:* it is a scope-decomposition of a measurement (which *domain* you measure the knob over), not a cause→parameter redirection. Weakest fit; included for completeness as a borderline.

**P4 — bad-plan vs bad-execution (the execution-fidelity gate).** `#def-strategic-calibration:36-38`.
- *Cause:* a positive edge residual $r_{ij}$.
- *Wrong knob:* revise the strategy $\Sigma_t$ (assume the plan is wrong).
- *Right knob:* without the execution-fidelity condition, "a positive residual could mean 'the plan is wrong' or 'the agent didn't follow the plan' … These require different corrections ($\Sigma_t$ revision vs execution improvement)."
- *Why Tier 3:* a real "which knob does this signal route to" caveat, but it is a *conditioning requirement on a definition* rather than a freestanding disambiguation result. Plus the segment's other content ($\delta_s$ vs $\delta_{\text{strategic}}$) is a two-quantities split adjacent to U1/S3.

---

## Explicitly excluded (and why) — so the boundary is auditable

- `#der-causal-insufficiency-detection` — a no-go theorem; it *is* Instance A of `#disc-constructive-impossibility-posture`. Sibling, not member.
- `#deriv-strategy-cost-regret-bound` (reverse-KL direction forced) — self-identifies as "the divergence-layer instance of `#disc-additive-coordinate-forcing`'s meta-pattern." Coordinate-forcing, not member.
- `#der-resource-bounded-destabilization` — a strengthen-to-theorem reframe ("the spiral is in the fuel, not the road"); no cause→wrong-knob conflation killed. Belongs to the constructive-impossibility / strengthen-first family.
- `#scope-edge-update-causal-validity` — the **inverse** move: observability ($\sigma_v\to0$) and identifiability ($\iota\to0$) are *two distinct causes that drive the same knob* ($\eta_{\text{edge}}\to0$). A unification, the mirror of this pattern. Worth holding in mind because the *combined* recognition "AAT keeps either splitting one cause across two knobs or merging two causes onto one knob" might be a cleaner framing than which-knob alone (see Assessment).
- `#def-adaptive-tempo` scalar-vs-tensor ("per-coordinate is unsafe when eigenbasis misaligns") — a scope/coordinate condition, not a cause→knob disambiguation.
- The `#disc-identifiability-floor` / `#disc-value-functional-grounding-floor` / `#disc-implementation-impossibility` cluster — boundary-facet floors; constructive-impossibility-posture territory.

---

## Count

- **Seeds:** 3 (S1, S2, S3) — all confirmed in canon, non-loss.
- **New Tier-1:** 2 (I1 emitter-scalar-vs-recipient-regime; I2 $\kappa$-vs-$\mathcal{A}$).
- **New Tier-2:** 2 (U1 $U_O$-vs-$U_\Sigma$; R1 exploration drives).
- **Tier-3 / partial:** 4 (P1 $\kappa$-scalar; P2 regime-vs-class; P3 codebase-$\rho$; P4 plan-vs-execution).

**Clean instances (seeds + Tier 1 + Tier 2): 7. With Tier-3 partials: up to 11.**

The seven clean instances span **all three depth-layers**: Part I (S1, R1), Part II (I1, S2, S3, U1), Part III (I2). It is not a Part-I-local quirk.

---

## Assessment and recommendation

**The set is coherent and large enough to be real — but it is not, by itself, a fifth cross-sectional meta-pattern, and the "which-knob" framing is slightly off-center.** My honest call has three parts.

**1. It clears the over-claiming-a-shallow-grouping bar.** Seven clean instances, derived independently across three parts and several authors, by two convergent gem-hunt agents plus the 471203-cycle recognition — that is genuine convergence, not three examples retrofitted. The strongest three (I1, I2, S1) are each load-bearing in their home segments and each kills a *real, named* error (I2 literally records the conflation as a fixed bug). This is not thin. A "too thin to name" verdict would be wrong, and I want to say that plainly given the task invited it.

**2. But the instances are heterogeneous in sub-shape, and "which parameter responds to which cause" only cleanly fits about half of them.** Two distinct sub-shapes are present:
   - *One-cause-wrong-knob* (the literal SP-26 framing): S1, I1, I2, R1, P1, P2, P3, P4 — a cause that a modeller would route to the wrong parameter.
   - *Two-distinct-quantities-a-naive-reading-merges*: S2, S3, U1 — where the move is "you think this is one quantity; it is two orthogonal ones with different remedies."

   Both kill a conflation and both route to different repairs, so they belong together — but the unifying *thing* is **"AAT refuses a tempting collapse and pins the correct causal routing of cause→remedy."** That is broader and truer than "which knob." A candidate reframing I'd put on the table (your call): **"diagnostic disambiguation"** or **"the anti-collapse discipline"** — *AAT repeatedly refuses to collapse two things a naive model would merge (one cause across two knobs; two causes onto one diagnostic), because the collapse hides a difference that routes to a different repair.* Note that this framing *also* naturally absorbs the inverse case (`#scope-edge-update-causal-validity`'s observability/identifiability *merge*), which "which-knob" cannot — the merge is the same discipline run the other direction (refuse to *split* what is really one knob, or refuse to *merge* what is really two). If you want the meta-pattern to be maximally true rather than maximally catchy, the anti-collapse framing is the one I'd reach for.

**3. Placement: this is a "Reading AAT" framing paragraph (OUTLINE preamble + README positioning), not a standalone `disc-*` meta-segment — at least not yet.** Reasoning, against the `#disc-separability-pattern` / `#disc-additive-coordinate-forcing` bar:
   - The genuine cross-sectional meta-segments each carry *derivable structural content* of their own (separability has the seven-ladder; coordinate-forcing has uniqueness theorems forcing the coordinate). This pattern carries **no theorem of its own** — like `#disc-constructive-impossibility-posture`, it is a *style/discipline recognition* ("here is a move the framework keeps making"). The honest precedent is therefore the constructive-impossibility-posture, which Joseph and the prior authors correctly classified as **"M1.5, not M5"** — a style claim explicitly *not* a fifth cross-sectional facet, placed alongside the meta-segments rather than parallel to the spine.
   - That precedent is the right template here. If it lands as a segment, it should be a **discussion-grade style segment in the same register as `#disc-constructive-impossibility-posture`** (named discipline + instance table + honest "this is a style, not a facet" scope note), *not* a claimed peer facet of the stability certificate. The two are natural siblings: constructive-impossibility-posture is "negative results as load-bearing apparatus"; this is "diagnostic disambiguation / anti-collapse as load-bearing apparatus." Both are *epistemic-architectural* recognitions, which is exactly the "integration not invention undersells this" point SP-26 makes.
   - Lowest-risk first move (matches PROPOSALS §H.4 "outlines are cheap"): land it as **one tight paragraph in the OUTLINE "Reading AAT" preamble + a sentence in the README positioning**, with the instance table held in the gem-hunt trail (this file) until/unless it earns a segment. That captures the positioning value (+4) immediately and at near-zero risk, and defers the segment-vs-paragraph decision until you've seen the set.

**Concrete recommendation.**
- *Do* name the pattern — it is real and convergence-validated. The deflation-avoidance discipline (`math-novelty-recognition`) applies: this is genuine clarifying novelty that the "integration not invention" line undersells.
- *Reframe* from "which-knob" to **anti-collapse / diagnostic-disambiguation** (it absorbs the two-quantities sub-shape and the inverse merge case, both of which "which-knob" leaves outside).
- *Place* it as a "Reading AAT" framing paragraph first (cheap, auditor-visible, immediate positioning value), with a `disc-*` **style segment** (sibling-register to `#disc-constructive-impossibility-posture`, explicitly *not* a fifth facet) as the natural home if you want the instance table in canon.
- *Anchor the segment, if landed, on the strongest three:* **I1** (emitter-scalar vs recipient-regime), **I2** ($\kappa$ vs $\mathcal{A}$, with the recorded-bug provenance), and **S1** ($\beta$ vs $\rho$). U1, S2, S3, R1 fill the table; P1–P4 are mentioned as adjacent/partial with the sibling-pattern overlap flagged so the boundary against separability/coordinate-forcing/constructive-impossibility stays clean.

**Bottom line:** not thin, not a new cross-sectional facet. It is a third member of AAT's epistemic-architectural style family (alongside constructive-impossibility-posture and the separability/forcing pair), best named as an anti-collapse / diagnostic-disambiguation discipline, and best introduced first as Reading-AAT framing prose with a constructive-impossibility-posture-style segment as the canonical home if you want one.
