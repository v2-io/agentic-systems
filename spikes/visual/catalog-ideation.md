# Diagram Catalog — Ideation Round 2 (Survey-Informed)

**Status.** Working artifact, ideation-grade. Sibling to (and supersedes the working assumptions of) the earlier informal catalog produced in the 2026-05-15 sector-cone calibration session. Built against [`msc/diagrams-and-comprehension-survey.md`](diagrams-and-comprehension-survey.md). Not yet a planning document — a re-ideation pass with the survey's filters applied.

## What changed from the prior catalog

The first catalog was organized by **section coverage** — every chapter got candidate figures, weighted roughly by the density of formal content. That implicit weighting is wrong for the design problem AAT actually faces. Under the survey's framework the right weighting is by **bottleneck-density per figure-slot**: where does comprehension *stall*, and which figure-slot most reduces the stall-rate. The two weightings agree on perhaps 30% of the catalog and disagree sharply on the rest.

Three concrete shifts:

1. **The preamble's mental-model figure ("measuring stick" / contraction-over-drift) jumps from "nice to have" to highest-priority single figure in the monograph.** Under coverage-weighting it sat alongside ~50 others. Under bottleneck-weighting it's the figure that determines whether the entire framework's organizing slogan is *perceivable* before a reader meets the first inequality. The Walton bathtub gloss, named in CLAUDE.md as the Feynman-criterion canonical example, is *the* test case of the survey's whole CRA-ladder + Larkin-Simon framework applied to AAT.

2. **The sector-cone, PSD-cone-with-facets, phase portraits, and most appendix figures drop sharply in priority.** They illustrate formal claims but rarely accelerate comprehension for non-already-control-theory readers. The 2026-05-15 sector-cone attempt is direct evidence: a control-theoretic convention-figure can be technically correct yet fail Larkin-Simon for the framework's actual reader profile. They should be deferred or replaced with concrete-anchored alternatives.

3. **Concrete-analog figures, small multiples, and concept maps emerge as under-exploited categories.** None of the three were prominent in the prior catalog; all three are well-evidenced by the survey (Mayer pre-training, Tufte small-multiples, Nesbit–Adesope concept-map meta-analysis at d = 0.66–1.08). For a monograph of AAT's reach, ~5–8 well-designed concrete-analog figures plausibly do more comprehension work than the other 40+ combined. Confidence: medium — claim follows the literature, but the magnitudes are extrapolated, not measured for AAT specifically.

## Caveats specific to AAT

Before the catalog itself, three frame conditions that affect every figure decision below.

**Audience profile, not generic novice.** The survey's empirical base is dominated by K-12 / introductory undergraduate / corporate training. AAT's reader profile is *theory-aware but not necessarily in this specific theory* — mathematicians, control theorists, ML researchers, philosophers of agency, applied causal-inference practitioners. The CRA ladder applies, but the right entry point varies by chapter: preamble and Findings briefs aim at the broad end (closest to novice for the framework); appendix derivations aim at the narrow end (closest to expert). One catalog cannot specify a single CRA target — the per-chapter calibration has to be made per figure. Confidence: high.

**Monograph genre, not textbook.** Monographs are compact, archival, prose-coupled, intended for re-reading. They earn the right to use abstract figures *if* the prose carries the concrete anchoring and the figure's role is reference rather than first-encounter comprehension. Bishop's *PRML* tolerates abundant figures because it's positioned as a graduate text; MacKay's *ITILA* uses sparse load-bearing figures; Spivak's *Calculus* uses figures only when essential. AAT's genre is closer to MacKay/Spivak than to PRML — sparse and load-bearing is the right discipline. This makes the bottleneck-density filter more aggressive. Confidence: medium-high; depends on Joseph's positioning choice.

**The Feynman / Larkin-Simon convergence.** CLAUDE.md's "respectful pedagogy" + Findings-brief Feynman criterion + the survey's Larkin-Simon perceptual-inference test + Bruner's CRA are four communities triangulating the same construct: *the diagram earns its slot when a sympathetic reader can see the conclusion before reading the prose, with the symbolic notation being a checked-against-the-formalism redundancy rather than the inferential pathway*. Naming this convergence explicitly tightens the rubric: any figure that doesn't pass this test is at best ornament, at worst implanted-wrong-schema (the sector-cone failure mode). Confidence: high.

## The five-tier rubric

Figures partition by *what they buy*, not by where they sit in the monograph.

### Tier 1 — Load-bearing comprehension figures

The 3–5 figures that earn their slot by carrying the framework's organizing principle into the reader's mental model. Highest investment. Each should pass the §VI 8-step protocol (and be revised until it does).

- **(T1-α) Measuring stick / contraction-over-drift scaffold.** Preamble. Concrete + representational. The Walton bathtub variant or a kinematic equivalent (a swing being pushed while a child stabilizes; a sailor tracking a drifting course). One panel; embedded in or immediately adjacent to the Reading AAT preamble. The figure that determines whether the certificate-existence anchor is perceivable before the reader meets any inequality. *Honesty constraint*: must be isomorphic, not merely evocative — perturbations of the analog must give predictions that hold against the formalism (measuring-stick = metric; flat direction = rank-deficient certificate; can't re-graduate = Sylvester; survives projection but leaks = Schur + memory term).

- **(T1-β) Orient cascade flowchart.** Part II, Ch.5. Abstract-grade, but already passes Larkin-Simon because the multi-step decision structure is exactly what flowcharts are good for. The reader can *see* which step happens next, which branches go where, and where the 2×2 diagnostic in step 3 attaches. Probably the only formal-content figure in the entire monograph that doesn't need a concrete companion.

- **(T1-γ) Strategy DAG worked example with AND/OR + edge credences.** Part II, Ch.3. Small graph (5–8 nodes), one AND node, one OR node, status propagation visible numerically. Demonstrates the propagation rule perceptually — reader can verify AND-multiplies and OR-1-minus-products on inspection.

- **(T1-δ) Bird's-eye concept map of AAT's organizing structure.** Appendix A or front matter. Higher level than the existing dependency-DAG SVGs (which show *segment dependencies*, not *concept relationships*). Shows the certificate spine as the center, the four facets as branches, the chapters as zones contributing to each facet. Provides navigation. Confidence in design: medium — this figure type is well-evidenced (Nesbit–Adesope) but the specific composition for AAT is unprototyped.

### Tier 2 — Chapter-level mental-model anchors

One concrete-or-representational figure per chapter preamble, sized to scaffold the chapter's central move before the reader meets its formalism. Lower investment per figure than Tier 1, but the *count* is structural — there should be one slot reserved per chapter.

| Chapter | Mental-model anchor (concrete → representational) |
|---|---|
| Part I Ch.1 (Coupled Loop) | A thermostat or commander as a feedback loop, with sensory and action channels labeled. |
| Part I Ch.2 (Reality Model) | History → state compression: a long journal compressed into a one-line summary, with sufficiency annotated. |
| Part I Ch.3 (Cycle in Motion) | Observe-update-act timeline with one event drawn, mismatch arrow shown. |
| Part I Ch.4 (Persistence) | The bathtub variant: faucet (drift) vs. drain (correction), overflow at $\rho > \alpha R$. Tier-1 anchor instantiated for this chapter; can re-use. |
| Part II Ch.1 (Lift to Purpose) | Agent-spectrum 2×2 with concrete agents in each cell (thermostat / PID / Kalman+LQR / LLM tool-user). |
| Part II Ch.2 (Causal Access) | Pearl's three-rung ladder with one shared example interpreted at each rung. |
| Part II Ch.3 (Strategy Structure) | Tier-1 strategy DAG instantiated for this chapter. |
| Part II Ch.4 (Strategy Dynamics) | Edge-credence update on a log-odds line, one before / one after. |
| Part II Ch.5 (Orient Cascade) | Tier-1 cascade flowchart. |
| Part III Ch.1 (Scope / Formation) | Composite-agent boundary: a sports team or herd shown twice, once as N sub-agents, once as one composite. |
| Part III Ch.2 (Composition Machinery) | "Zooming out" cartoon: micro-trajectories projected to macro-trajectory, with the closure-defect gap visible as the discrepancy. |
| Part III Ch.3 (Unity / Communication) | Unity radar with one team's profile shown vs. another's. |
| Part III Ch.4 (Cooperative / Adversarial) | Tug-of-war vs. handshake — same machinery, opposite signs of $\gamma$. |
| Part III Ch.5 (Strategic Composition) | Two-agent equilibrium concrete (Cournot-style); 16-cell composition grid for the formal version. |

Note: several of these may collapse into Tier 1 if they're load-bearing for cross-chapter reading rather than chapter-local.

### Tier 3 — Comprehension-accelerator figures at specific bottlenecks

Figures justified by a specific *§3.2 bottleneck*. Each should be designed only after the bottleneck has been verified by either (a) a sympathetic reader actually stalling there or (b) the prose's own structure naming an inferential gap. The §VI rubric applies, but full progressive-disclosure design is not always warranted at this tier.

Candidates that have a high prior of passing this filter:
- Directed-separation three-box diagram (Part II, Ch.1) — only after a concrete analog (intelligence-vs-operations separation, or a Kalman + LQR split) is paired.
- Satisfaction-gap × control-regret 2×2 (Part II, Ch.3) — table is probably enough; perceptual inference works on tables. Consider whether a figure is even needed.
- Correlation Hierarchy ladder as small multiples (L0 → L1 → L1' → L2), each showing the same example DAG with one augmentation added.
- Wrapping construction (Part III, Ch.2) — Class 3 component inside Class 1 wrapper, goal-blind query interface highlighted. Concrete companion: "PROPRIUM auxilia hierarchy" or "shoshin's parsed-response wrapper."
- 4-regime recipient-side decomposition as small multiples (4 panels, one regime each, same example).
- Wrapping W₀ / W₁ / W₂ regimes side-by-side.

### Tier 4 — Illustrate-but-don't-perceptualize

Figures that illustrate a formal claim without actually shortening the comprehension path. Acceptable to defer; if drawn, lowest investment (don't iterate to camera-ready, accept v1).

- Sector-cone two-panel (already drafted; control-theoretic convention). Replace with concrete contraction-race cartoon for first-encounter contexts; retain the abstract version only in the appendix.
- Phase portraits in general (effects spiral, equilibrium convergence) — same caveat.
- Helmholtz–Hodge / Sylvester / Mori–Zwanzig obstruction illustrations — interesting to the differential-geometer reader, archival otherwise.
- Variational sector / Fisher-Rao bias-bound curves.
- Multi-timescale singular-perturbation nesting.
- Lyapunov ellipsoid as standalone.

### Tier 5 — Deferrable, decorative, or actively counterproductive

Figures that look obligatory but fail one or more tests. Naming them explicitly prevents accidental investment.

- An *abstract* "PSD cone with four facets" without a concrete companion — fails Larkin-Simon (the cone is itself an abstract object the reader hasn't met).
- Scope lattice as a Venn / inclusion picture — table or prose is denser and clearer.
- "Modularity-state-dynamics three-operation" figure before the M4 segment lands — premature.
- Agent spectrum 2×2 *unfilled* (just labeled quadrants without examples) — adds nothing the prose doesn't carry; close to chartjunk.
- Multi-timescale nesting as a pictorial — table-like already; figure adds nothing.
- "OODA inside opponent's loop" as a literal cycle diagram — the prose carries the temporal claim directly; a figure here would be decorative.
- Information-bottleneck rate-distortion plane — well-known to anyone who needs it, opaque to anyone who doesn't.

Listing these is not an editorial judgment about importance — these claims still matter; they just don't reward figure-design effort.

## Cross-cutting opportunities

**Small-multiples slots** the prior catalog underweighted:
- Lyapunov contraction over time (concentric sublevel sets at successive snapshots).
- Strategy DAG before/after L0 → L1 augmentation.
- 4-regime recipient-side decomposition (4 panels, one regime each).
- GUC Class 1 / 2 / 3 architectures (3 panels, same task).
- Pearl-hierarchy rungs (3 panels with same example at different levels).
- Wrapping construction at W₀ / W₁ / W₂ regimes.
- Convention hierarchy C1 / C2 / C3 on the same satisfaction-gap calculation.

Tufte's small-multiples principle is one of the better-evidenced design moves in the survey (§V), and AAT has at least 7 natural slots for it. Probably 3–4 of these should actually be drawn; the others are listed to inform decisions about which.

**Concrete-analog figures worth dedicated design effort:**
- The measuring stick / bathtub (T1-α; Walton's contribution).
- The thermostat / commander (loop).
- The journal-keeper (compression to state).
- The sports team / playbook (composition).
- The tug-of-war / handshake (signed coupling).
- The sailor tracking a drifting course (persistence under non-stationarity).

Each of these is a candidate "preamble-to-the-preamble" — the scaffold a reader can carry into the chapter. Note that the same analog can serve multiple chapters: the bathtub serves Persistence, the sailor serves any disturbance-rejection content, the sports team serves the entire composition arc.

**Concept-map opportunities** (higher-level than dep-graphs):
- The certificate spine + four facets (T1-δ).
- The GUC class × scope-condition lattice.
- The Correlation Hierarchy as concept map (L0 → L1 → L1' → L2 with what's identified at each level).
- The convention hierarchy and what diagnostic each tier permits.

These are different from the existing `dep-graph-*.svg` files. The dep-graphs show *which segments depend on which*; concept maps show *which ideas live near which other ideas*. Both have a role; AAT only has the former.

## §VI 8-step rubric, demonstrated on T1-α (measuring stick scaffold)

1. **Structural parse.** The preamble names a dynamical relationship (target drifts, agent corrects) plus an existence-equivalence claim (certificate ⟺ exponential stability). Two structures: process + theorem.
2. **Bottleneck.** "Contraction-rate exceeds drift-rate" is the slogan but the reader has no concrete referent for "rate." Abstract quantification over rates is the bottleneck.
3. **Diagram-type.** Concrete analog → perceptually grounded process diagram. Bathtub fits: faucet rate = drift; drain rate = correction; water-level = error; overflow = persistence failure.
4. **Concreteness ladder.** Stage 1 concrete (bathtub picture, no symbols). Stage 2 representational (same bathtub annotated with $\rho$, $\alpha\|\delta\|$, $R$). Stage 3 abstract (the formal inequality, cross-referenced to Stage 2). Three small panels, left-to-right.
5. **Structural sketch.** Bathtub silhouette; faucet labeled "drift $\rho$"; drain labeled "correction $\alpha\|\delta\|$"; water-level marked $\|\delta\|$; rim line at $R$.
6. **Signaling.** Color: drift and correction in contrasting hues, persisting through all three panels. Arrows on faucet (in) and drain (out) sized roughly to their rates. The rim-line in Stage 2 and 3 carries a separate signal color.
7. **Minimalism audit.** Strip any tile/grout/decoration on the bathtub. Strip shadows. Strip background. Keep only: silhouette, faucet, drain, water level, rim line, labels.
8. **Progressive disclosure.** Three panels left-to-right; reader meets concrete first, abstract last; the abstract panel's inequality $\alpha > \rho/R$ is the conclusion the first two panels were preparing the reader to *see*.

Pass: yes, by design. Investment: ~half-day of iteration to camera-ready, plus prose alignment with surrounding preamble.

## §VI 8-step rubric, demonstrated on T1-β (orient cascade flowchart)

1. **Structural parse.** Multi-step decision process with branches and conditional re-entry. Pure process structure.
2. **Bottleneck.** The cascade has 5 numbered steps with sub-branches (4a/4b/4c, 5a–5d) and a 2×2 diagnostic at step 3. Prose alone forces the reader to construct the branching structure mentally.
3. **Diagram-type.** Flowchart. Larkin-Simon test passes natively for this content type.
4. **Concreteness ladder.** Representational level is sufficient — the steps are already named operationally ("evaluate $\delta_{\text{sat}}$", "evaluate $\delta_{\text{regret}}$"); no further concretization needed.
5. **Structural sketch.** 5 sequential boxes (the steps) on a left-to-right axis. Step 3 has a branching 2×2 inset. Step 4 has three sub-boxes (4a/4b/4c). Step 5 has four sub-options. Backward arrows from 4c and 5b to indicate re-evaluation.
6. **Signaling.** Color: the 4 cells of the step-3 diagnostic each get a color that propagates to the appropriate downstream step (e.g., "strategy problem" cell color matches the path through 4a/4b).
7. **Minimalism audit.** No box shadowing, no 3D, no decoration. Use uniform box sizes except for genuine hierarchical differences. Labels on boxes only, no separate legend.
8. **Progressive disclosure.** Two versions: a *minimal* version (5 main steps, no sub-branches) in the chapter intro; a *full* version (with 4a/4b/4c and 5a/5d) inline at the segment.

Pass: yes. Investment: less than T1-α since this is a flowchart, a well-known convention.

## What was overweighted in v1 and dropped here

- The PSD-cone-with-four-facets *as a single abstract figure*. (Demoted to T5; the concept-map version T1-δ replaces its function with concrete-anchored navigability.)
- The sector cone two-panel composition. (Demoted to T4; the bathtub variant at T1-α and the chapter-anchor for Ch.4 cover its comprehension role.)
- Helmholtz–Hodge / Sylvester / Mori–Zwanzig as separate appendix figures. (Demoted to T4–T5; the prose carries these.)
- The variational-sector / Fisher-Rao curves. (T4.)
- Most appendix derivations getting their own figure. (T5: prose suffices for archival use.)

## Open questions

1. **Audience calibration per chapter.** Where does each chapter actually sit on the novice-to-expert axis? My estimates above are inferences from the OUTLINE; Joseph can recalibrate.
2. **The bathtub vs. alternative scaffolds.** Walton's bathtub is one option. The sailor / swing / kinematic alternatives may be more or less honest to the formalism. The honesty test should be applied to each before commitment.
3. **Whether the concept-map (T1-δ) belongs in the front matter or in Appendix A.** Front-matter placement gives it preamble visibility but commits the reader to a navigation framework before they've earned it; appendix placement keeps it as reference.
4. **How many Tier-2 anchors actually survive review.** My 14 listed candidates are speculative; the real count is probably 6–9 after rubric application.
5. **The "sympathetic reader" test.** The Walton experience suggests one or two outside-mathematician-practitioner first-readers are worth recruiting *before* significant figure investment, to identify actual bottlenecks rather than imagined ones.

---

*Honesty note.* I'm extrapolating from the survey's empirical base (mostly introductory instructional design) to AAT's reader profile (theory-aware monograph audience). The directional claims are well-supported; specific figure-count estimates (~10–15 camera-ready vs. ~50 in the prior catalog) are inferences I'd downgrade to medium confidence pending real Joseph-side bottleneck identification. The rubric is solid; the population it applies to is the variable.
