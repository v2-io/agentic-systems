# Prior-Art Analysis: Constructive Impossibility and the Identifiability Floor

> [!note]
> **Refreshed 2026-05-21.** The previous version of this file was a generic two-paragraph "no-gos as identifiability floors" sketch that omitted (a) the five-step formal pattern stated in `disc-identifiability-floor.md`; (b) the four specific instances with their named external theorems; (c) the Sylvester's-law-of-inertia recognition that supplies the rank-collapse irreducibility mechanism; (d) the distinction between rank-collapse and projection-closure obstructions; and (e) the IB-side relationships to `disc-separability-pattern`, `disc-stability-certificate`, and `disc-constructive-impossibility-posture`. This file now reflects the segment's actual content.

**Target Claim:**
AAT exhibits a recurring meta-pattern across at least three (officially counted as four, with Instance 4 currently marked KNOWN-DEFECTIVE pending Joseph-reserved disposition) independently-derived results. The pattern has a five-step shape:

1. **Setting** — name an inferential task (detect a structural property, identify a parameter, distinguish two model classes) under a specific information regime;
2. **External theorem** — invoke an established information-theoretic limit independent of AAT (Pearl/Bareinboim Causal Hierarchy Theorem; Cramér-Rao bound on Fisher information; Liberzon-class common-Lyapunov nonexistence; Čencov invariance);
3. **No-go** — the external theorem forbids the task under the specified regime;
4. **Boundary characterization** — the conditions under which the regime fails (i.e., the agent has *more* information than the regime allows) admit identification; these boundary routes map onto specific AAT machinery the theory already requires;
5. **Strengthened consequence** — the floor elevates that AAT machinery from "useful" to "the unique broadly-available violation of the regime," and therefore *load-bearing* for the theory.

For the rank-collapse subclass of floors (Instances 1 and 2), a single classical theorem — **Sylvester's law of inertia** — supplies the irreducibility mechanism: the agent's representational freedom is exactly the congruence orbit on the Fisher-information operator ($\mathcal G \mapsto S^\top \mathcal G S$), and Sylvester's law states that congruence preserves inertia. A rank-deficient information operator is rank-deficient in every coordinate; no reparameterization escapes the floor. The only escape is *rank augmentation* — a new measurement (intervention, side channel, observable witness) — which is *not* a coordinate change. Instance 3 is a *different* obstruction: composition is a non-invertible projection, so its no-go is a Schur-complement / memory-kernel statement, not an inertia statement. This plurality of mechanism is itself why the floor pattern is a presentational family rather than a single theorem.

---

## 1. State of the Field & Scientific Precedence

The closest direct ancestor for the *methodological posture* — using impossibility results constructively to characterize regime-specific scope and named structural escapes — is the Pearl/Shpitser/Bareinboim causal-identifiability program. Other relevant lineages give the per-instance external theorems AAT imports.

### Pillar 1: The Causal Identifiability Program (the closest methodological precedent)
The Pearl-Shpitser-Bareinboim line states the "regime → impossibility → structural escape" posture in almost exactly the form AAT uses, for one family of problems (causal identification, transportability, data fusion):
- **Pearl (1995)** *Causal diagrams for empirical research* — already states the methodological posture in unusually explicit terms: causal diagrams are not passive summaries of assumptions but **active devices for determining whether available assumptions suffice, and if they do not, for suggesting what extra observations or auxiliary experiments would make the inference possible**. Extraordinarily close to AAT's intended methodological tone.
- **Shpitser & Pearl (2008)** *Complete Identification Methods for the Causal Hierarchy* — complete graphical characterization of when causal queries are or are not computable from lower-level data.
- **Bareinboim & Pearl (2012)** *Causal Inference by Surrogate Experiments: z-Identifiability* — extending the same logic to surrogate experiments.
- **Bareinboim & Pearl (2012, 2013)** transportability completeness results; **Bareinboim & Pearl (2016)** *Causal inference and the data-fusion problem*.
- **Shpitser & Tchetgen (2014)** *Causal Inference with a Graphical Hierarchy of Interventions* — node/edge/path interventions as a structured hierarchy.
- **Lee, Correa & Bareinboim (2019, 2020)** general identifiability + general transportability.
- **Bareinboim, Correa, Ibeling & Icard (2022)** Causal Hierarchy Theorem — the exact external theorem AAT imports for Instance 1.

The causal program is a strong exact precedent for *one family* of constructive-impossibility moves. AAT's claim is that the same methodological discipline operates across multiple non-equivalent theorem families.

### Pillar 2: External Theorems AAT Imports per Instance
Each AAT identifiability-floor instance imports a *published external theorem* whose role is to forbid the inference. The contribution is the AAT-side recognition of which setting falls within which theorem, not re-derivation.

- **Bareinboim et al. (2022)** Causal Hierarchy Theorem → Instance 1 (on-policy L0 insufficiency detection in `#der-causal-insufficiency-detection`).
- **Cramér (1946)** Fisher-information bound → Instance 2 (L1' mixture identifiability from single-channel observations in `#deriv-edge-credence-dynamics` Prop B.7).
- **Liberzon (2003)** *Switching in Systems and Control* §2.1 common-Lyapunov nonexistence; **Dayawansa & Martin (1999)** explicit $2 \times 2$ counterexample; **Shorten, Wirth, Mason, Wulff & King (2007)** *SIAM Review* survey → Instance 3 (composite contraction certification from component marginals in `#deriv-critical-mass-composition` / `#result-contraction-template`).
- **Čencov (1982)** invariance theorem → Instance 4 (the currently-KNOWN-DEFECTIVE entry, see note below).

### Pillar 3: Information-Constrained Control (a distributed analogue)
Stabilization under finite feedback rate gives a structurally similar pattern (regime → impossibility → richer-channel escape) but is not as exact a methodological precedent as the Pearl-Bareinboim program:
- **Tatikonda & Mitter (2004)** *Control under communication constraints* — IEEE TAC.
- **Nair & Evans (2004)** *Stabilizability of Stochastic Linear Systems with Finite Feedback Data Rates* — SIAM J. Control Optim.
- **Sahai & Mitter (2006)** *Anytime Capacity for Stabilization* — IEEE Trans. Info. Theory.

These contribute to the broader claim that constructive use of impossibility is a real methodological pattern in adjacent fields.

### Pillar 4: Sylvester's Law and the Fisher-Information Congruence (the irreducibility mechanism)
The rank-collapse irreducibility mechanism (Instances 1, 2) is classical:
- **Sylvester (1852)** *Phil. Mag.* — the law of inertia: every invertible real congruence preserves the number of zero, positive, and negative eigenvalues of a quadratic form.
- **Horn & Johnson (2013)** *Matrix Analysis* (2nd ed.), Thm 4.5.8 — standard modern statement.
- **Lehmann & Casella (1998)** *Theory of Point Estimation* (2nd ed.), §2.5 — the Fisher-information reparameterization law $\mathcal G_\varphi = S^\top \mathcal G_\theta S$ that makes every coordinate change a congruence.

All three are textbook material. AAT's contribution is the *recognition* that the agent's entire representational freedom is exactly the Fisher-congruence orbit, which makes Sylvester's law (rather than per-instance computation) the source of the rank-collapse irreducibility. Sylvester is not AAT-novel; the *application* to the integrated agent-theoretic floor pattern appears to be.

---

## 2. Key Anchor Papers Identified

1. **Pearl, J. (1995).** *Causal diagrams for empirical research.* (Biometrika 82:669) — DOI 10.1093/BIOMET/82.4.669
   *Significance:* States the constructive-impossibility methodological posture for causal identification in almost the form AAT uses cross-family. The closest exact methodological precedent.
2. **Bareinboim, Correa, Ibeling & Icard (2022).** *On Pearl's Hierarchy and the Foundations of Causal Inference.*
   *Significance:* The Causal Hierarchy Theorem AAT imports for Instance 1. Provides the formal statement that L2 distinctions are not in general identifiable from L1 data.
3. **Cramér, H. (1946).** *Mathematical Methods of Statistics.* Princeton University Press.
   *Significance:* The Fisher-information / Cramér-Rao bound used in Instance 2's refutation calculation.
4. **Liberzon, D. (2003).** *Switching in Systems and Control*, Theorem 2.1; **Dayawansa & Martin (1999)** *IEEE Trans. Automat. Control* 44:751.
   *Significance:* Common-Lyapunov nonexistence for switched linear systems. The external theorem AAT imports for Instance 3's composite-contraction-from-marginals no-go.
5. **Sylvester, J. J. (1852).** *Phil. Mag.* 4(23):138–142.
   *Significance:* The inertia-invariance theorem that supplies the rank-collapse floor's irreducibility mechanism. Recognized 2026-05-14 as the unifying mechanism behind Instances 1 and 2.
6. **Shpitser & Pearl (2008).** *Complete Identification Methods for the Causal Hierarchy.* JMLR 9:1941.
   *Significance:* The completeness side of the Pearl-Bareinboim methodological tradition.
7. **Sahai & Mitter (2006).** *Anytime Capacity for Stabilization.*
   *Significance:* Information-constrained-control analogue of the constructive-impossibility pattern (stabilization impossible below capacity threshold; richer feedback structure is the named escape).

---

## 3. Conclusion on Novelty & Overlap

The methodological posture has very strong prior art for the *causal-identification* family (Pillar 1). The per-instance external theorems are all published outside AAT (Pillar 2). The Sylvester recognition uses a 1852 textbook theorem (Pillar 4). The information-constrained-control analogue gives a distributed precedent for the broader move (Pillar 3).

**Where AAT actually contributes:**

1. **Cross-family unification (synthetic novelty — the strongest center).** No close prior paper in the search surfaces a *cross-instance meta-framework* that runs the same five-step shape across causal-identification, estimation floors, contraction certification from marginals, and parameterization-invariance. The Pearl-Bareinboim program does this superbly within causal inference; the AAT move is to elevate the pattern to a framework-level discipline across multiple non-equivalent theorem families. This is what the memo identifies as the "highest novelty candidate."

2. **The Sylvester-recognition (mathematical recognition).** Identifying the agent's representational freedom as exactly the Fisher-congruence orbit, and the rank-collapse floors as the boundary of the positive-definite information cone that congruence cannot cross, converts per-instance "we checked no reparameterization escapes" calculations into one named classical mechanism. This is not novel mathematics in the sense of new theorem-derivation, but it is novel *recognition* — and the recognition has analytical content: it bounds its own scope by *distinguishing* the rank-collapse mechanism from Instance 3's projection-closure obstruction, which is a Schur-complement / memory-kernel statement, not an inertia statement.

3. **Each instance's per-derivation contribution.** Instance 1's derivation is exact for shallow strict-prerequisite cases and robust qualitative for general DAG topology (`#der-causal-insufficiency-detection`). Instance 2's Fisher rank-1 calculation is exact (`#deriv-edge-credence-dynamics` Prop B.7). Instance 3's symmetric-matched-Tier-1-scalar counterexample is exact within the stated setup (`#deriv-critical-mass-composition` / `#result-contraction-template`). These are theorem-grade per-instance results that import external machinery (CHT, CR bound, common-Lyapunov nonexistence) into AAT-internal settings — Nash-style work: new results using established machinery, not re-derivation of the machinery.

4. **The strengthened-consequence content (architectural novelty).** Each floor *elevates* a specific piece of AAT machinery from useful to load-bearing:
   - Instance 1 elevates `#der-loop-interventional-access` (Pearl-Level-2 evidence from ordinary acting) from "useful machinery" to "the unique broadly-available violation of the on-policy detection no-go."
   - Instance 2 elevates observability-as-information-augmentation from a convenience to a theoretical prerequisite for L1' identifiability.
   - Instance 3 elevates `#deriv-critical-mass-composition` (matched-Tier composition-contraction certificate) and the composite-extended interventional access to load-bearing status under heterogeneous-Tier composites; `#scope-composite-agent` itself acquires *enabling status* because scope-satisfaction is what positions the composite within a regime where any of the four structural escapes can operate.

**Status of Instance 4 (the currently-KNOWN-DEFECTIVE entry).** The fourth instance — universal information-to-distance constant under non-(PI) norms via heteroscedastic-Gaussian counterexample — is marked KNOWN-DEFECTIVE in `disc-identifiability-floor` §"Current Instances." Its prerequisite segment `#deriv-observation-ambiguity-bias-bound` itself states *in canon* that the no-go "does not match the five-element test for a floor instance … a *single* escape … the honest position: this no-go is a **downstream theorem of the (PI) commitment, not a new floor instance**." An independent recheck (`spikes/spike-identifiability-floor-instance4-resolution-2026-05-18.md`) finds that the slot conflated two distinct objects — the downstream (PI) theorem (not a floor) and a genuine architecturally-distinct / behaviorally-identical floor (the rho Regime-C confound and the CL-2 reserved refinement). Resolution is Joseph-reserved. Pending that resolution, the floor count is **three confirmed plus one contested**, not four.

**Where AAT does *not* claim novelty:**
- The methodological posture for the causal-identification family (Pearl 1995, Shpitser & Pearl 2008, Bareinboim line).
- Sylvester's law itself (1852 classical theorem).
- The external theorems imported per instance (CHT, Cramér-Rao, common-Lyapunov nonexistence, Čencov invariance) — all published outside AAT.
- The general posture that impossibility results can be used constructively (broad lineage across statistics, control theory, computer science).

**Connections to other meta-segments.**
- `disc-separability-pattern` carries the *positive half* (separable-core / structured-repair / general-open across seven ladders); the identifiability-floor instances have positive counterparts there (Instance 1 ↔ observable-sibling-covariance structured-repair in correlation ladder; Instance 2 ↔ observable-$C$ / facilitator-monotonicity structured-repair in same ladder).
- `disc-stability-certificate` is the unifying spine: this segment is its *boundary facet* (where the certificate drops rank; the rank-collapse Sylvester argument). The other facets are `disc-separability-pattern` (scope-of-existence facet) and `disc-additive-coordinate-forcing` (forced-identity facet — row 12 territory).
- `disc-constructive-impossibility-posture` names the cross-instance *style recognition* atop the boundary facet — five cleanly-fitting instances of the "name the floor, name the unique escape, treat the no-go as load-bearing apparatus" posture, of which the M1 instances here are the principal cases.

**Epistemic status of the load-bearing segment.** `disc-identifiability-floor.md` is `status: discussion-grade` *at the meta-pattern level* (it organizes already-derived results into a recognized family; the recognition is presentational, not theorem-derivation). *Individual instances retain higher status*: Instance 1 is *exact for shallow strict-prerequisite cases* and *robust qualitative for general DAGs*; Instance 2's Fisher rank-1 refutation is *exact*; Instance 3's counterexample is *exact within the symmetric-matched-Tier-1-scalar setup* and *robust qualitative for general heterogeneous composites*. The Sylvester-recognition is *discussion-grade* presentational recognition of a classical mechanism.

**Novelty profile (per the meta-summary's four-axis rubric):**
- *Math Novelty:* **Some.** The Sylvester-recognition (analytical content distinguishing rank-collapse from projection-closure mechanisms) plus the per-instance theorem-grade derivations import-and-apply external machinery to AAT-internal settings — Nash-style derivations. Not "new math" in the sense of new techniques; new results using established techniques in named ways.
- *Arch Novelty:* **High.** The strengthened-consequence content — each floor elevating a specific AAT machinery to load-bearing — is a structural architectural claim. The meta-pattern is the boundary facet of the stability-certificate spine.
- *Synth Novelty:* **High.** The cross-family unification (causal-identifiability + estimation floors + contraction-from-marginals + invariance) under one constructive-impossibility discipline is the strongest novelty center per the Undermind memo.
- *Appl Novelty:* **None.** No application-level instantiation in this meta-segment (per-instance segments link to applications but those are scored against their own rows).
- *Impact:* **High.** Memo rates impact "moderate but real," with high impact if the constructive-impossibility posture is seen as distinctive and reusable. The connection to the stability-certificate spine (`disc-stability-certificate`) and to the broader scope-honesty discipline of AAT positions this meta-pattern as a signature framework move.
