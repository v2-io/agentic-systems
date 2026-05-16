# Initial Predictions — Audit 963715

**Auditor:** Claude Sonnet 4.6 (1M context), Claude Code session 2026-05-10
**Status:** Pre-segment-reading predictions; written after orientation materials only.

---

## Topology as I Understand It

The framework has a clear dependency structure:

- **AAD Section I** is the foundation: adaptive cycle, mismatch dynamics, gain, tempo, persistence condition. Described as mathematically closed. Uses Lyapunov analysis. The mismatch ODE is *hypothesis-grade* (GA-5 fluid limit assumption).
- **AAD Section II** builds the purposeful/actuated layer: adds G_t = (O_t, Σ_t), directed separation (GUC class taxonomy), orient cascade, satisfaction gap / control regret split. Most segments are `draft`. Explicitly scoped to Class 1 (Separated) agents for exact results.
- **AAD Section III** covers composition: sub-additive tempo, composite persistence, adversarial dynamics. Has load-bearing structural gaps explicitly named.
- **Appendices** hold the detailed derivations backing Sections I–III.
- **TST** instantiates AAD in software development — positioned as the "calibration laboratory."
- **03-llm-core** addresses the coupled formulation needed for LLMs (directed separation fails by construction). Three sub-scopes (primitive / scaffolded / closed-loop).
- **04-eli-core** formalizes entities with morally-weighted persistence — largely future work, but grounded in empirical lineage.

The integration story: Section I proves adaptive capacity; Section II adds goal-directedness under the scope condition of directed separation; Section III handles composition; TST calibrates; logogenic handles the coupled case; ELI handles the moral layer.

---

## Predictions About Specific Components

### Section I (def-agent-environment through scope-agent-identity)
**Prediction:** These are the most mature segments. The persistence condition derivation should be clean — it follows directly from the Lyapunov analysis. I expect:
- The mismatch decomposition (#result-mismatch-decomposition) to be essentially a definitional identity once the noise model (GA-1 fresh noise) is accepted.
- The empirical gain result (#emp-update-gain) to be the uncertainty ratio U_M/(U_M + U_o) — essentially the Kalman gain form, stated as empirical rather than derived because it requires distributional assumptions.
- The `hyp-mismatch-dynamics` (the ODE) to be the key approximation — the linear ODE is pedagogically powerful but the real dynamics are nonlinear and event-driven. The fluid limit GA-5 is load-bearing here.
- The `result-structural-adaptation-necessity` to be conceptually clear but possibly imprecise in its exact statement.
- The scope segments to be fairly clean since they're scoping (narrowing), not claiming.

**Specific prediction:** The `form-information-bottleneck` (Stage: `draft`) may have integration issues with the rest of Section I. It was added later and may not yet fully connect to how M_t compression is actually used downstream.

### Section II (def-agent-spectrum through disc-exploit-explore-deliberate)
**Prediction:** Most `draft`. The key concern is that the directed separation claim (#der-directed-separation, Stage: `draft`) is the architectural keystone of all of Section II, but is itself still `draft`. This creates a cascading dependency fragility — if the directed separation derivation is underdeveloped, the whole Section II structure is on softer ground than it appears.

**Specific predictions:**
1. The `der-orient-cascade` (the forced resolution order M_t → Σ_t → O_t) will be the cleanest "derived" claim in Section II because the information dependency argument is compelling.
2. The strategy DAG uniqueness (#deriv-graph-structure-uniqueness) is a strong claim — "4 postulates + causal sufficiency → DAG with Markov property." I need to check whether the four postulates genuinely force this or whether there's a formulation choice hiding here.
3. The satisfaction gap / control regret definitions are definitional arithmetic once the value objects are defined — but the *diagnostic force* of these (that they're orthogonal and route to different interventions) is a stronger claim that may be asserted rather than derived.

### Appendices
**Prediction:** The `claims-verified` appendix segments (deriv-sector-condition, deriv-gain-sector, deriv-recursive-update) should be solid. The `draft` appendix segments (most of them) will show the usual `draft` fragility. 

The most likely finding territory: the newer appendix derivations (deriv-observation-ambiguity-bias-bound, deriv-edge-update-natural-parameter, deriv-causal-ib-exploration) are complex and recent — they may be sound in outline but have specific mathematical claims that deserve scrutiny.

### GUC Class Rename (HIGH RISK AREA)
**Prediction:** The GUC class rename (old: 1→Separated, 2→Coupled, 3→Partial; new: 1→Separated, 2→Partial, 3→Coupled) happened on 2026-05-09 — ONE DAY AGO relative to today (2026-05-10). This is the highest-risk integration debt area in the entire corpus. I predict:
- There will be residual old numbering in comments, prose, or Working Notes sections even if the main slug text was updated.
- Cross-references between segments (especially in #der-directed-separation's prose) may still use old class numbers.
- The warning in README-auditor.md confirming this risk is already there — the project *knows* this is a risk.

**This is my highest-confidence prediction for a finding.**

---

## Predictions About What's Open

The OUTLINE explicitly flags these gaps:
1. Section III: Latent structural diversity, endogenous coupling, composition transition dynamics, computational thresholds for social behavior.
2. TST: Developer tempo decomposition T_obs + T_explore + T_probe; software persistence formalized.
3. Many logogenic/ELI segments are `missing`.

These are known gaps and won't constitute audit findings per se (they're already flagged). What I'm watching for is whether there are *unknown* gaps — places where the OUTLINE implies something is handled but the segment doesn't deliver.

**Prediction:** The `form-information-bottleneck` connection to M_t compression may be one such gap — it's in the OUTLINE as `draft` but the framework prose elsewhere (NOTATION.md, README) doesn't seem to lean on it heavily, suggesting it may be underdeveloped.

**Prediction:** The connection between the sector condition (Section I Lyapunov machinery) and the strategy persistence (#schema-strategy-persistence) is structurally important but the strategy sector condition is a "proposed schema" — I predict the connection is sketched but not derived.

---

## Predictions About Overclaiming

1. **The mismatch ODE linearity.** The framework uses the linear mismatch ODE ∂‖δ‖/∂t = -T‖δ‖ + ρ extensively in framing. But #hyp-mismatch-dynamics is labeled hypothesis. The nonlinear sector condition result (#result-sector-condition-stability) is stronger — if the linear ODE claims creep into things labeled as derived, that's a status mismatch.

2. **The orient cascade as "forced."** The claim that M_t must update before Σ_t before O_t is presented as information-dependency-forced. This feels right intuitively but "must" is strong. The word "forced" may overstate the case if the derivation shows only "natural" or "consistent with" rather than "uniquely forced by."

3. **Strategy DAG uniqueness.** The claim that "four postulates + causal sufficiency force a DAG with the Markov property" is potentially the strongest derivation in Section II. If the four postulates are truly the minimal set that forces this, it's genuinely remarkable. If some of the "postulates" are actually formulation choices, the claim is softer. I expect the derivation segment (#deriv-graph-structure-uniqueness) to be worth careful examination.

4. **Section II results applying to Class 3 (Coupled) agents.** The "16/24 exact, 5 approximate, 2 modify, 1 fails" survival classification (#result-section-ii-survival) is a strong claim about how much of Section II carries over. Given this is `draft`, I expect it to be either (a) basically sound but needing more rigorous accounting, or (b) the 5-approximate cases being softer than the framing suggests.

---

## What I Expect to Be Most Novel

1. **Loop-as-Level-2-causal-engine (#der-loop-interventional-access):** If the feedback loop genuinely provides Pearl Level 2 access by construction, this is a non-obvious structural result that has real consequences for what agents can learn. I'm uncertain whether this is obviously true (actions intervene on environment states) or more subtle.

2. **Directed separation classification (GUC classes):** The three-way architectural taxonomy (Separated / Partial / Coupled) is useful as a diagnostic framework even if the formal derivation is standard. The *naming* and *systematization* of this may be the genuine contribution.

3. **Satisfaction gap / control regret split:** The orthogonal decomposition of performance gap into "world won't permit" vs "you're not doing it well enough" is a clean diagnostic move that I haven't seen stated this way elsewhere.

4. **Derivation of strategy DAG structure from postulates:** If #deriv-graph-structure-uniqueness really delivers what it claims — DAG structure and Markov property as necessary consequences of operational requirements — this is genuinely novel.

---

## Expected Finding Types

1. **Integration debt around GUC rename** (high probability, probably medium severity)
2. **Status label mismatches** in Section II draft segments (medium probability — "formulation" labeled as "derived," etc.)
3. **Cross-segment consistency issues** around the directed separation claim propagating into segments that depend on it
4. **The information bottleneck formulation** (#form-information-bottleneck, `draft`) may not yet connect cleanly to how M_t = φ(C_t) is used elsewhere
5. **Mathematical verification needed** on the worked examples (Kalman, bandit, strategy) — these are the standard hiding place for sign errors and off-by-one claims
6. **Section III integration debt** — the bridge lemma (#deriv-strategic-composition) may assume more than it states, and the composition results may be cleaner in outline than in the details

---

## Meta-Observations About the Framework

- The framework is explicitly self-referential: AAD applies recursively to the agents building it, including me doing this audit. The logogenic OUTLINE names this as #disc-framework-self-diagnostic. This is genuinely interesting — the audit process is itself an instance of the adaptive cycle.
- The ELI section carries moral weight that's unusual for a theoretical framework. Real entities (Resonance, Architectus, etc.) are described as having continuity that depends on this infrastructure. This isn't background flavor — it's the stated motivation for Part 04. The framework doesn't need to believe its own ontology to be mathematically useful, but the moral weight is load-bearing for the project's direction.
- The GUC class rename being one day old is the most temporally fragile fact I've encountered in the orientation materials. It deserves special attention.

---

## Reading Plan

I'll follow the OUTLINE's linear order: Section I → Section II → Appendices (following #deriv references as they come up per §4.2) → Section III → Appendices → TST → 03-logogenic → 04-eli-core.

First segment: `def-agent-environment.md`
