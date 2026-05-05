# Separability-Ladder Standalone Paper — Proposal

**Status:** Working draft, exploratory. Joseph-anointed paper-candidate per 2026-05-04 conversation. Subsumes the *B-N-Sep* portfolio entry from `~/src/ops/papers/03-asf-tier2-and-cross-segment.md` so the agentic-systems repo carries the canonical home for the paper proposal; the ops entry can be retained as a portfolio pointer or trimmed.

**Cross-references:**
- **Source segment:** [`01-aad-core/src/disc-separability-pattern.md`](../01-aad-core/src/disc-separability-pattern.md) — *(queued rename: `discussion-separability-pattern` → `discussion-separability-ladder`, see naming-rename-plan)*
- **Prior-art search report:** [`ref/separability-ladder-prior-art-report.md`](../ref/separability-ladder-prior-art-report.md) — Undermind, 31-paper full-text sweep, 2026-05-04
- **Naming-cycle queue:** [`msc/naming/naming-rename-plan.md`](naming/naming-rename-plan.md) §"Deferred to refined Round 1 / Round 2" + §"Pending subject-noun renames — surfaced post-R2"
- **Companion meta-segments:** [`#disc-identifiability-floor`](../01-aad-core/src/disc-identifiability-floor.md) (negative-half complement); [`#disc-additive-coordinate-forcing`](../01-aad-core/src/disc-additive-coordinate-forcing.md) (constructive half — meta-architectural triad partner)

---

## Thesis

**The separability ladder is a cross-domain meta-pattern: across structurally distinct sources of intractability in applied mathematics, a recurring three-rung trichotomy organizes positive-half identification claims.** Each rung commits to a specific epistemic posture — separable core (clean cases), structured repair (recovery under named bounded-cost augmentation), general open (intractable / non-identifiable). The pattern recurs across at least seven AAD-internal hierarchies (Pearl's causal hierarchy, convention C1/C2/C3, architecture Class 1/2/3, contraction Tier 1/2/3, identification Regime A/B/C, scope adaptive/agency/composite, A2'-scope α₁/α₂/β) and is recognizable in adjacent literatures (statistical identification, parameterized complexity, ill-posed inverse problems, restricted-intervention causality).

The contribution sits at three layers:

1. **Recognition** that the trichotomy is the same shape across structurally distinct sources of intractability — not a coincidence, not domain-specific
2. **Formalization** of the bounded-cost-repair operator that defines the middle rung — what Hintikka 1991's identifiability trichotomy gestures at but doesn't explicit
3. **Cross-domain extension** — observing the same template recurring across N+1 applied-math hierarchies, not just one

The framework's *complementarity claim* — that the separability ladder paired with `#disc-identifiability-floor` (the no-go-theorem half) gives scope-honest theorizing the structural duality it needs — is itself a candidate philosophical contribution.

---

## Verdict from prior-art search (Undermind, 2026-05-04)

Verified depth: *targeted* — 31 papers full-text read, broader candidates checked at abstract/metadata level. Search depth report at `ref/separability-ladder-prior-art-report.md`.

**Direct answer:** No exact named cross-domain meta-pattern found.

**Closest neighbors:**

| Source | Their formalization | Relation to target |
|---|---|---|
| **Hintikka 1991** *("Towards a General Theory of Identifiability")* | Theory-alone *definability* / theory-plus-empirical *identifiability* / *non-identifiability* | **Strongest older abstract anchor.** Same tripartite shape; lacks the explicit bounded-cost repair operator and cross-domain ladder claim. |
| **Pearl/Shpitser ID lineage** *(Pearl 1995; Shpitser-Pearl 2006/2008; Bareinboim-Pearl 2012/2014; Lee-Correa-Bareinboim 2019)* | Identifiable / augmentation-identifiable (z-id, transportability, g-id) / hedge-blocked | **Most-developed within-domain instance.** The ID algorithm IS this template. Each repair regime adds a named augmentation (surrogate experiment, selection diagram, arbitrary experiment). |
| **Robins-Richardson-Shpitser 2020** *(interventionist mediation)* | Clean case / structured repair via intervention decomposition / recanting-witness obstruction | **Cleanest in-domain cite-and-extend anchor.** Explicit no-go + repair + decomposition pattern within a specific identification setting. |
| **Bareinboim 2022** *("On Pearl's Hierarchy and the Foundations of Causal Inference")* | Pearl's hierarchy as logical and epistemic hierarchy; comparisons to formal-language and complexity hierarchies | **Cross-hierarchy meta-discussion at N=2-3.** Closest to the cross-domain abstraction but stops short — treats Pearl as distinctively logical, not as one instance of a general template. |
| **Basse-Bojinov 2020** *("A general theory of identification")* | Identifiable / partially-identified / strongly-non-identifiable regimes | **Best modern formal abstraction across fields.** Lacks the bounded-cost repair operator as middle rung. |
| **Maclaren-Nicholson 2019** *("What can be estimated?")* | Well-posed / regularization-recoverable / ill-posed | **Best dual-structure cross-field neighbor.** Centers on stability/regularization rather than structured-repair operators. |
| **Restricted-intervention lineage** *(Robins 1986; Richardson 2013 SWIGs; Dawid 2000/2020; Richardson-Robins 2023)* | Treatment-regime semantics / SWIGs / decision-theoretic intervention nodes | **Patches the missing-prior-art gap on `#scope-edge-update-causal-validity`-flavored regime restrictions.** Establishes prior art for structured/feasibility-restricted interventions. |
| **Stensrud et al. 2019** *(separable effects in competing events)*; **Díaz 2022** *(non-agency interventions)*; **Robins-Richardson 2010** *(alternative graphical models)* | Decomposable separable effects / dismissible pathways / expanded-graph identification | **Strong neighboring recurrence inside causal identification.** Pattern recurs in mediation, competing-events, edge-intervention settings within the wider causal-identification literature. |
| **Hoover 2012** *(philosophy of modeling)*; **Iwasaki-Simon 1994** *(causality and model abstraction)* | Hierarchies of models; near-decomposability; well-made-toaster vs repairman cases | **Strong philosophy / Simon-line parallels.** Aggregation, model articulation. Not formal tractability/identifiability ladders. |
| **Downey-Fellows 1995/1999** *(parameterized complexity)*; **Simpson 1999** *(reverse mathematics)* | FPT / W[t] / paraNP-hard; subsystem strengths (RCA₀, WKL₀, ACA₀, ATR₀, Π¹¹-CA₀) | **Best formal hierarchy-of-strength literatures.** Verified weak connection to applied-identifiability ladders. |

---

## Paper structure (after deeper prior-art map)

1. **Hintikka 1991 as the historical abstract anchor.** Open with Hintikka's tripartite identifiability framework — *definable / identifiable / non-identifiable* — and locate it in the broader history of identifiability theorizing (econometrics origin per Hintikka §2; logical formalization per Hintikka §3+).
2. **Pearl-lineage as the most-developed instance.** Walk Shpitser-Pearl 2006/2008 ID completeness; Bareinboim-Pearl 2012/2014 transportability and z-identifiability; Lee-Correa-Bareinboim 2019 g-identifiability with arbitrary surrogates. Show each is an instance of the trichotomy with a named bounded-cost augmentation operator.
3. **Neighboring recurrence inside causal inference.** Robins-Richardson-Shpitser 2020 mediation; Stensrud et al. 2019 competing events; Díaz 2022 non-agency; restricted-intervention lineage Robins 1986 / Richardson 2013 / Dawid 2000-2020 / Richardson-Robins 2023. Pattern recurs *inside its closest-related field*, not just at AAD's framing.
4. **Cross-domain recurrence.** The 7 AAD-internal hierarchies (Pearl + convention + architecture + contraction + identification regime + scope + metric). Each hierarchy fills in the trichotomy slots (separable / repair / open) with its own structural conditions. The pattern is structural, not domain-specific.
5. **Theorem-schema (formal).** Tripartite partition $P = P_{\text{sep}} \sqcup P_{\text{rep}} \sqcup P_{\text{open}}$ + three companion theorems: separable-core identification, structured-repair identification under named augmentation, general-open no-go (witnessed by external information-theoretic theorem).
6. **Adjacent abstractions that stop short.** Bareinboim 2022 (Pearl ↔ formal-language ↔ complexity, three-hierarchy comparison without the ladder); Basse-Bojinov 2020 (general theory of identification, identification-region not repair-ladder); Maclaren-Nicholson 2019 (ill-posed inverse problems as cross-field pattern, without bounded-cost-repair middle rung); Hoover 2012 (philosophy of modeling, hierarchies-of-models without formal tractability ladder); Iwasaki-Simon 1994 (causality and model abstraction, near-decomposability without the trichotomy).
7. **Discussion + open questions.** The strong "any scope-honest theory making exact-under-conditions claims plus broader-coverage claims must instantiate this trichotomy or an equivalent" claim is a candidate scope-honesty theorem; left to future work. The complementarity with the identifiability-floor pattern (negative-half no-go theorems) as a unified dual structure for scope-honest theorizing.

---

## Strategic positioning

> *"Extending Hintikka's tripartite identifiability framework with formal bounded-cost repair operators, and observing the same trichotomous shape recurring across N additional applied-math hierarchies."*

Much sharper than *"we propose a novel meta-pattern"*. The cite-and-extend posture is the strongest available given the prior-art landscape:

- **Cite Hintikka 1991** for the abstract historical anchor (tripartite identifiability; predates the modern causal-inference formulations)
- **Extend** by formalizing the bounded-cost repair operator that Hintikka gestures at but doesn't explicit
- **Generalize** by demonstrating the recurrence across N additional applied-math hierarchies that Hintikka didn't anticipate

**Cite-and-extend anchors:**
- **In-domain (causal inference):** Robins-Richardson-Shpitser 2020 *(interventionist mediation; cleanest target for the cite-and-extend move within causality)*
- **Meta-discussion (Pearl as one of several hierarchies):** Bareinboim 2022 *(extends Bareinboim's hierarchy-comparison move to N=7+ hierarchies and adds the cross-cutting ladder structure)*
- **Abstract historical (general identifiability):** Hintikka 1991 *(extends with bounded-cost-repair operator and cross-domain recurrence)*

---

## Effort

**4-6 weeks** (modestly increased from earlier 3-5 estimate after the deeper prior-art map).

**Reading list (focused; ~half-day to one day of reading when drafting starts):**
- Hintikka 1991 — *acquired locally* at `ref/towards-a-general-theory-of-identifiability.pdf`
- Robins-Richardson-Shpitser 2020 *(IM in ACM Books / 10.1145/3501714.3501754)*
- Bareinboim et al. 2022 *(R-60, ACM Books — acquired locally at `ref/bareinboim-2022-pearl-hierarchy.pdf`)*
- Basse-Bojinov 2020 *("A general theory of identification")*
- Maclaren-Nicholson 2019 *(arXiv 1904.02826)*
- Hoover 2012 *("Causal structure and hierarchies of models")*
- Robins 1986 *("Treatment regime mortality studies" — acquired locally at `ref/robins-1986-treatment-regime-mortality-studies.pdf`)*
- Dawid 2000 *("Causal inference without counterfactuals" — acquired locally at `ref/dawid-2000-causal-inference-without-counterfactuals.pdf`)*

Several PDFs already locally available; remaining acquisitions are tractable through standard channels.

---

## Venue analysis

| Tier | Venue | Rationale |
|---|---|---|
| **Primary** | **Journal of Causal Inference (JCI)** | Bareinboim, Robins, Richardson, Pearl publish there. Paper extends a conversation editors are steeped in; fit with Robins-Richardson-Shpitser 2020 cite-and-extend posture is exact. |
| Secondary | **Synthese** | Broader philosophy of science; tolerant of cross-domain abstraction work; Hintikka-lineage venue. |
| Tertiary | **Philosophy of Science** | Iwasaki-Simon and Hoover lineage lives there. |
| Tertiary | **Erkenntnis** | Plausible alternate philosophy-of-science venue. |

---

## Strategic value (high)

- **Zero welfare-claim attack surface** — pure structural philosophy of applied math, immune to current AI-discourse hostility around consciousness / AI welfare claims
- **Distinct venue ecosystem** from anything else in the publication portfolio — opens new editor/reviewer relationships
- **Independent-researcher credibility** in causal-inference and philosophy-of-science venues that other portfolio papers don't reach
- **Verified novel by independent prior-art search** — Undermind 31-paper full-text sweep returned no direct anticipation
- **Withdrawn Ghassami-Shpitser 2021 partial-intervenability paper is informative** — the field is reaching for this abstraction and hasn't crystallized it; the standalone paper can productively engage with that gap
- **Joseph-anointed paper-candidate** per 2026-05-04 conversation

---

## Cluster relations

- **Independent of the welfare/consciousness clusters** in the publication portfolio — clean isolation from AI-welfare-discourse risk
- **Loosely related to** the *B-M-Combined: AAD Methodology Paper* (M1 + M2 + M3 unified) but **standalone-publishable**. The unified methodology paper bundles the three meta-architectural patterns (identifiability floor / separability ladder / additive-coordinate-forcing) under a single framework methodology framing; the standalone separability-ladder paper extracts and develops the M2 pattern as its own contribution
- **Partner with `#disc-identifiability-floor`** — the negative-half companion. The two patterns together give scope-honesty its structural form; one paper might mention the other as complementary; both are extractable separately

---

## Open question — naming of the three rungs

The family name `Separability Ladder` (replacing `Separability Pattern` per Round-1 consensus rationale that "ladder" is more evocative for the three-rung shape) is settled and queued in the rename plan.

The **three rung-names** are under consideration for refinement (decision pending Joseph as of 2026-05-04):

| Triad option | Rung names | Rationale |
|---|---|---|
| **Status quo** | separable core / structured repair / general open | Project-distinctive; minor grammatical asymmetry ("general open" is adj+adj, others are modifier+noun) |
| **Minimal fix** | separable core / structured repair / open frontier | Fixes grammatical asymmetry; minimal corpus change |
| **Hintikka echo (exact)** | definable / identifiable / non-identifiable | Maximum cite-and-extend leverage with Hintikka 1991; tight three-word triad |
| **Hintikka echo (parallel)** | definable core / identifiable region / non-identifiable frontier | Hintikka echo with maintained modifier+noun parallel structure; cleanest cite-and-extend posture for paper framing |
| **Operational shape** | direct / augmented / open | Names the augmentation-presence structure; Pearl-lineage echo |

**Lean (this document's draft moment):** *Hintikka echo (parallel)* — `definable core / identifiable region / non-identifiable frontier`. Maximizes the paper's cite-and-extend leverage (the paper opens with Hintikka's trichotomy and extends with bounded-cost repair operator + cross-domain recurrence), maintains parallel structure across the three rungs, and the small extension over Hintikka's narrow "auxiliary empirical results" augmentation to AAD's broader "named structural augmentation" is a real generalization the paper can flag explicitly.

**Decision deferred** — Joseph wanted time to think more on the rune-naming. This proposal is ready to draft against either the status-quo names (no rebrand) or any of the alternates (modest rebrand cost in the corpus).

---

## What this proposal does NOT yet contain

- A draft of the actual paper. This document is the strategic plan; the paper itself is the next artifact.
- Detailed paper outline (section-by-section with target word counts).
- Co-author conversations. The paper is a single-author candidate per current planning.
- Specific submission timeline. Effort estimate is 4-6 weeks of focused work; calendar timing is open.

## Status of completion

This proposal is intended to be the canonical home for the separability-ladder paper proposal in the agentic-systems repo. The B-N-Sep section in `~/src/ops/papers/03-asf-tier2-and-cross-segment.md` (lines 112-145ish) carried the strategic-portfolio framing that this document fully subsumes. The ops file can retain a one-line pointer to this proposal or be edited as part of separate ops-portfolio maintenance; nothing in ops is now load-bearing for this paper that isn't in this proposal or the segment Working Notes.
